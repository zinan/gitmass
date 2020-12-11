import requests


class BaseAdapter(object):
    def __init__(self, params=None):
        self.params = params
        self.result = {"success": True, "message": "", "results": []}
        print('{} loaded.'.format(self.__class__.__name__))

    def check_param(self):
        if self.params is None:
            self.result["message"] = "ERROR! Necessary params are empty. Exiting..."
            self.result["success"] = False
            return self.result

    def process_request(self, url, params=None, function=None, *args, **kwargs):
        r = requests.get(url, params=params, **kwargs)
        if r.status_code == 200 and r.json():
            function(r.json())
            self.result["success"] = True
        else:
            self.result["success"] = False
            self.result["message"] = "ERROR! Please check your organization and/or access token! Exiting..."
        return self.result
