#!/usr/bin/env python3
""" A module for testing the client module. """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test git orgClient """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'login': 'example'})
    def test_org(self, org_name, mock_get_json):
        """ client get json """
        client = GithubOrgClient(org_name)
        org_data = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(org_data, {'login': 'example'})
