from unittest import TestCase

from adapters.BaseAdapter import BaseAdapter


class TestBaseAdapter(TestCase):
    def test_check_param(self):
        obj = BaseAdapter()
        result = obj.check_param()
        expected_message = "ERROR! Necessary params are empty. Exiting..."
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])

    def test_process_request(self):
        params = {"token": "11111", "org": "dummy", "user": "foo",
                  "url": "https://api.bitbucket.org/2.0/repositories/%s?pagelen=100"}
        obj = BaseAdapter(params)
        expected_message = "ERROR! Please check your organization and/or access token! Exiting..."
        result = obj.process_request(params["url"])
        self.assertEqual(result["message"], expected_message)
        self.assertEqual(False, result["success"])
