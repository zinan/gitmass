from unittest import TestCase

from adapters import GithubAdapter


class TestGithubAdapter(TestCase):
    def setUp(self):
        self.obj = GithubAdapter()
        self.params = {"token": "11111", "org": "dummy", "user": "foo", "url": "github.com"}

    def test_get_repos_params_none(self):
        result = self.obj.get_repos()
        expected_message = "ERROR! Necessary params are empty. Exiting..."
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])

    def test_get_repos_success(self):
        self.obj = GithubAdapter(self.params)
        expected_message = "ERROR! Please check your organization and/or access token! Exiting..."
        result = self.obj.get_repos()
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])
