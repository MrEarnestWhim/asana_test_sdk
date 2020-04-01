from .provider import AsanaCore


class AsanaPOST(AsanaCore):
    def create_section(self, project_gid, params=None):
        if params is None:
            params = {}

        return self.post(f'/projects/{project_gid}/sections', params)

    def add_task(self, section_gid, params=None):
        if params is None:
            params = {}

        return self.post(f'/sections/{section_gid}/addTask', params)

    def create_task(self, params=None):
        if params is None:
            params = {}

        return self.post('/tasks', params)

    def create_project(self, params=None):
        if params is None:
            params = {}

        return self.post('/projects', params)
