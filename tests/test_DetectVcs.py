from unittest import TestCase

from helpers.DetectVcs import DetectVcs


class TestDetectVcs(TestCase):
    def test_detect(self):
        obj = DetectVcs("https://github.com")
        expect_url = "https://api.github.com"
        response = obj.detect()
        self.assertEqual(expect_url, response["api_url"])

        obj = DetectVcs("https://gitlab.com")
        expect_url = "https://gitlab.com/api/v4/projects"
        response = obj.detect()
        self.assertEqual(expect_url, response["api_url"])

        obj = DetectVcs("https://api.bitbucket.org/2.0/repositories")
        expect_url = "https://api.bitbucket.org/2.0/repositories"
        response = obj.detect()
        self.assertEqual(expect_url, response["api_url"])
