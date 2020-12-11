from unittest import TestCase

from adapters import GitlabAdapter


class TestGitlabAdapter(TestCase):
    def setUp(self):
        self.obj = GitlabAdapter()
        self.params = {"token": "11111", "org": "dummy", "user": "foo", "url": "https://gitlab.com"}

    def test_get_repos_params_none(self):
        result = self.obj.get_repos()
        expected_message = "ERROR! Necessary params are empty. Exiting..."
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])

    def test_get_repos_success(self):
        self.obj = GitlabAdapter(self.params)
        expected_message = "ERROR! Please check your organization and/or access token! Exiting..."
        result = self.obj.get_repos()
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])
