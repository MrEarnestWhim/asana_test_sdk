from .provider import AsanaCore


class AsanaPUT(AsanaCore):
    def task(self, task_gid, params=None):
        if params is None:
            params = {}

        return self.put(f'/tasks/{task_gid}', params)

    def section(self, section_gid, params=None):
        if params is None:
            params = {}

        return self.put(f'/sections/{section_gid}', params)

    def project(self, project_gid, params=None):
        if params is None:
            params = {}

        return self.put(f'/projects/{project_gid}', params)
