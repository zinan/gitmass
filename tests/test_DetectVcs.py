from unittest import TestCase

from helpers.DetectVcs import DetectVcs


class TestDetectVcs(TestCase):
    def test_detect(self):
        self.assertTrue(True)

    def test_detect_github(self):
        obj = DetectVcs("https://github.com")
        expect_url = "https://api.github.com"
        result = {}
        obj.detect_github(result)
        self.assertEqual(expect_url, result["api_url"])

    def test_detect_gitlab_v4(self):
        obj = DetectVcs("https://gitlab.com")
        expect_url = "https://gitlab.com/api/v4/projects"
        result = {}
        obj.detect_gitlab_v4(result)
        self.assertEqual(expect_url, result["api_url"])

    def test_detect_gitlab_v3(self):
        obj = DetectVcs("https://gitlab.com")
        expect_url = "https://gitlab.com/api/v4/projects"
        result = {}
        obj.detect_gitlab_v4(result)
        self.assertEqual(expect_url, result["api_url"])

    def test_detect_bitbucket(self):
        obj = DetectVcs("https://api.bitbucket.org/2.0/repositories")
        expect_url = "https://api.bitbucket.org/2.0/repositories"
        result = {}
        obj.detect_bitbucket(result)
        self.assertEqual(expect_url, result["api_url"])
