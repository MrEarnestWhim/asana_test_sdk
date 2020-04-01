from django.contrib import admin

from asana_app.models import Task, Project, Sections


class MyAdmin(admin.ModelAdmin):
    readonly_fields = (
        'gid',
    )
    list_display = (
        'name',
        'gid',
    )


@admin.register(Task)
class Admin(MyAdmin):
    pass


@admin.register(Project)
class Admin(MyAdmin):
    pass


@admin.register(Sections)
class Admin(MyAdmin):
    pass
