from .provider import AsanaCore


class AsanaGET(AsanaCore):
    def me(self):
        return self.get('/users/me')

    def sections_in_project(self, project_gid):
        return self.get(f'/projects/{project_gid}/sections')

    def projects(self):
        return self.get('/projects')

    def workspaces(self):
        return self.get('/workspaces')
