#!/usr/bin/env python3
"""test_client module
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import patch, PropertyMock, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """test the  org method's return value"""
        expected_response = {}
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        org_data = client.org

        expected_url = client.ORG_URL.format(org=client._org_name)
        mock_get_json.assert_called_once_with(expected_url)

        self.assertEqual(org_data, expected_response)

    def test_public_repos_url(self):
        """Tests the _public_repos_url method
        """
        target_property = "client.GithubOrgClient.org"

    # Use patch to replace the org property with a mock
        with patch(target_property, new_callable=PropertyMock) as mock_org:
            expected_response = {"repos_url": "example"}
            mock_org.return_value = expected_response
            client = GithubOrgClient("google")
            result = client.org
            self.assertEqual(result, expected_response)
