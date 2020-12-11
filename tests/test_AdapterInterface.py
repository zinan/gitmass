#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from adapters import GithubAdapter


class TestAdapterInterface(TestCase):

    def test_original_dict(self):
        hc = GithubAdapter()
        self.assertIsInstance(hc, GithubAdapter)
