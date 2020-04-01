from .get import AsanaGET
from .post import AsanaPOST
from .put import AsanaPUT


class AsanaInit:
    get = AsanaGET()
    put = AsanaPUT()
    post = AsanaPOST()

    def __init__(self):
        """
        For fast response in admin panel
        """
        self.result_workspaces = self.get.workspaces().get('data', {})
        self.result_user = self.get.me().get('data', {})
        self.result_projects = self.get.projects().get('data', {})
        self.result_sections = self.get.sections_in_project(
            self.result_projects[0].get('gid')
        ).get('data', {})


AsanaAPI = AsanaInit()
