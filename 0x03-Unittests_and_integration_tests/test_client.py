#!/usr/bin/env python3
"""Test for client.GithubOrgClient class"""
import unittest
from parameterized import parameterized, parameterized_class
from client import (
    GithubOrgClient,
)
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Test GithubOrgClient.org."""
        client = GithubOrgClient(org_name)
        client.org()
        mock.called_with_once(client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "something"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
        
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos."""
        

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)