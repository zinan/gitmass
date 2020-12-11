from adapters.BaseAdapter import BaseAdapter


class GitlabAdapter(BaseAdapter):
    def __init__(self, params=None):
        super().__init__(params)

    def get_repos(self):
        super(GitlabAdapter, self).check_param()
        if self.result["success"]:
            super(GitlabAdapter, self).process_request(
                '%s/api/v4/projects?per_page=999&simple=true&private=true' % self.params['url']
                , headers={'PRIVATE-TOKEN': '%s' % self.params['token']}
                , function=self.parse_response
                )
        return self.result

    def parse_response(self, json):
        [self.result["results"].append({'name': item['name'], 'url': item['ssh_url_to_repo']}) for item in json]
