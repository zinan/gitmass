import requests
import tldextract
import validators


class DetectVcs:
    def __init__(self, url):
        self.url = url
        domain = tldextract.extract(self.url)
        self.domain = domain.domain+'.'+domain.suffix

    def detect(self):
        result = {'api_url': "", 'adapter': ""}
        valid = validators.url(self.url)
        if not valid:
            raise RuntimeError(f'The url {self.url} is not valid!')

        result = self.detect_gitlab_v3(result)
        result = self.detect_gitlab_v4(result)
        result = self.detect_bitbucket(result)
        result = self.detect_github(result)

        return result

    def detect_github(self, result):
        github_url = f'https://api.{self.domain}'
        github = validators.url(github_url)
        if github and self.domain == 'github.com':
            r = requests.get(github_url)
            if r.status_code == 200 and r.json():
                result['adapter'] = "Github"
                result['api_url'] = github_url
                return result

    def detect_gitlab_v4(self, result):
        gitlab_v4_url = f'{self.url}/api/v4/projects'
        gitlab_v4 = validators.url(gitlab_v4_url)
        if gitlab_v4:
            r = requests.get(gitlab_v4_url)
            if r.status_code == 200 and r.json():
                result['adapter'] = "Gitlab"
                result['api_url'] = gitlab_v4_url
                return result

    def detect_gitlab_v3(self, result):
        gitlab_v3_url = f'{self.url}/api/v3/projects'
        gitlab_v3 = validators.url(gitlab_v3_url)
        if gitlab_v3:
            r = requests.get(gitlab_v3_url)
            if (r.status_code == 200 or r.status_code == 401) and r.json():
                result['adapter'] = "Gitlab"
                result['api_url'] = gitlab_v3_url
                return result

    def detect_bitbucket(self, result):
        bitbucket_url = f'https://api.{self.domain}/2.0/repositories'
        bitbucket = validators.url(bitbucket_url)
        if bitbucket:
            r = requests.get(bitbucket_url)
            if (r.status_code == 200 and r.json()) or self.domain == "bitbucket.org":
                result['adapter'] = "Bitbucket"
                result['api_url'] = bitbucket_url
                return result
