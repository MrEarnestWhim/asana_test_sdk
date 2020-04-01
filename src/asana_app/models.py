from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from asana_project.asana_sdk import AsanaAPI


class Project(models.Model):
    gid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(max_length=255)


class Sections(models.Model):
    gid = models.CharField(max_length=100, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)


class Task(models.Model):
    gid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(max_length=255)
    notes = models.TextField(max_length=100)
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE)
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


@receiver(pre_save, sender=Project)
def project_save(sender, instance, **kwargs):
    if not instance.id:
        response = AsanaAPI.post.create_project(params={
            "name": instance.name,
            "workspace": AsanaAPI.result_workspaces[0].get('gid')
        }).get('data', {})
        instance.gid = response.get('gid')
    else:
        AsanaAPI.put.project(instance.gid, params={
            "name": instance.name,
        })


@receiver(pre_save, sender=Sections)
def sections_save(sender, instance, **kwargs):
    if not instance.id:
        response = AsanaAPI.post.create_section(instance.project.gid, params={
            "name": instance.name,
        }).get('data', {})
        instance.gid = response.get('gid')
    else:
        AsanaAPI.put.section(instance.gid, params={
            "name": instance.name,
        })


@receiver(pre_save, sender=Task)
def task_save(sender, instance, **kwargs):
    if not instance.assignee.id:
        instance.assignee.gid = AsanaAPI.result_user.get('gid')
        instance.assignee.name = AsanaAPI.result_user.get('name')

    if not instance.id:
        response = AsanaAPI.post.create_task(params={
            "projects": [
                instance.sections.project.gid
            ],
            "name": instance.name,
            "notes": instance.notes,
            "assignee": instance.assignee.gid,
            "workspace": AsanaAPI.result_workspaces[0].get('gid')
        }).get('data', {})
        instance.gid = response.get('gid')
        AsanaAPI.post.add_task(instance.sections.gid, params={'task': instance.gid})
    else:
        AsanaAPI.put.task(instance.gid, params={
            "name": instance.name,
            "notes": instance.notes,
        })
