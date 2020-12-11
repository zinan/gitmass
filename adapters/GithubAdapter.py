from adapters.BaseAdapter import BaseAdapter


class GithubAdapter(BaseAdapter):
    def __init__(self, params=None):
        super().__init__(params)

    def get_repos(self):
        super(GithubAdapter, self).check_param()
        if self.result["success"]:
            super(GithubAdapter, self).process_request('https://api.github.com/orgs/%s/repos?per_page=999' %
                                                       self.params['org']
                                                       , headers={'Authorization': 'token %s' % self.params['token']}
                                                       , function=self.parse_response
                                                       )
        return self.result

    def parse_response(self, json):
        [self.result["results"].append({'name': item['name'], 'url': item['ssh_url']}) for item in json]
