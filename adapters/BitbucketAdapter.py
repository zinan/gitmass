from adapters.BaseAdapter import BaseAdapter


class BitbucketAdapter(BaseAdapter):
    def __init__(self, params=None):
        super().__init__(params)

    def get_repos(self):
        super(BitbucketAdapter, self).check_param()
        if self.result["success"]:
            super(BitbucketAdapter, self).process_request('https://api.bitbucket.org/2.0/repositories/%s?pagelen=100' %
                                                          self.params['org']
                                                          , auth=(self.params['user'], self.params['token'])
                                                          , function=self.parse_response
                                                          )
        return self.result

    def parse_response(self, json):
        [self.result["results"].append({'name': item['name'], 'url': item['links']['clone'][1]['href']}) for item in
         json['values']]
