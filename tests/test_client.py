import os
import unittest

import requests
from nstbrowser import NstbrowserClient
from unittest.mock import patch, Mock


class TestNstbrowserClient(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
        self.client = NstbrowserClient(api_key=self.api_key)

    def test_initialization(self):
        self.assertEqual(self.client.api_key, self.api_key)
        self.assertEqual(self.client.api_address, "http://localhost:8848/api/v2")

    @patch("nstbrowser.client.requests.request")
    def test_get_request(self, mock_request):
        """Test GET request with and without parameters"""
        expected_response = {"key": "value"}
        mock_resp = Mock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_request.return_value = mock_resp

        # Test GET without parameters
        response = self.client._get("/test")
        mock_request.assert_called_with(
            "get",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            params=None,
        )
        self.assertEqual(response, expected_response)

        # Test GET with parameters
        params = {"param1": "value1", "param2": "value2"}
        response = self.client._get("/test", params=params)
        mock_request.assert_called_with(
            "get",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            params=params,
        )
        self.assertEqual(response, expected_response)

    @patch("nstbrowser.client.requests.request")
    def test_post_request(self, mock_request):
        """Test POST request with dictionary and list data"""
        expected_response = {"key": "value"}
        mock_resp = Mock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_request.return_value = mock_resp

        # Test POST with dictionary data
        dict_data = {"data": "value"}
        response = self.client._post("/test", data=dict_data)
        mock_request.assert_called_with(
            "post",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=dict_data,
        )
        self.assertEqual(response, expected_response)

        # Test POST with list data
        list_data = ["item1", "item2"]
        response = self.client._post("/test", data=list_data)
        mock_request.assert_called_with(
            "post",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=list_data,
        )
        self.assertEqual(response, expected_response)

        # Test POST with no data
        response = self.client._post("/test")
        mock_request.assert_called_with(
            "post",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=None,
        )
        self.assertEqual(response, expected_response)

    @patch("nstbrowser.client.requests.request")
    def test_put_request(self, mock_request):
        """Test PUT request with dictionary and list data"""
        expected_response = {"key": "value"}
        mock_resp = Mock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_request.return_value = mock_resp

        # Test PUT with dictionary data
        data = {"data": "value"}
        response = self.client._put("/test", data=data)
        mock_request.assert_called_with(
            "put",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=data,
        )
        self.assertEqual(response, expected_response)

        # Test PUT with list data
        list_data = ["item1", "item2"]
        response = self.client._post("/test", data=list_data)
        mock_request.assert_called_with(
            "put",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=list_data,
        )
        self.assertEqual(response, expected_response)

        # Test PUT without data
        response = self.client._put("/test")
        mock_request.assert_called_with(
            "put",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=None,
        )
        self.assertEqual(response, expected_response)

    @patch("nstbrowser.client.requests.request")
    def test_delete_request(self, mock_request):
        """Test DELETE request with dictionary and list data"""
        expected_response = {"key": "value"}
        mock_resp = Mock()
        mock_resp.json.return_value = expected_response
        mock_resp.raise_for_status.return_value = None
        mock_request.return_value = mock_resp

        # Test DELETE with dictionary data
        dict_data = {"data": "value"}
        response = self.client._delete("/test", data=dict_data)
        mock_request.assert_called_with(
            "delete",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=dict_data,
        )
        self.assertEqual(response, expected_response)

        # Test DELETE with list data
        list_data = ["item1", "item2"]
        response = self.client._delete("/test", data=list_data)
        mock_request.assert_called_with(
            "delete",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=list_data,
        )
        self.assertEqual(response, expected_response)

        # Test DELETE with no data
        response = self.client._delete("/test")
        mock_request.assert_called_with(
            "delete",
            f"{self.client.api_address}/test",
            headers={"x-api-key": self.api_key},
            json=None,
        )
        self.assertEqual(response, expected_response)

    @patch("nstbrowser.client.requests.request")
    def test_request_error_handling(self, mock_request):
        mock_request.side_effect = requests.RequestException("Error")

        with self.assertRaises(RuntimeError) as context:
            self.client._get("/test")

        self.assertIn(
            "Error in [TestNstbrowserClient.test_request_error_handling]: Error",
            str(context.exception),
        )
