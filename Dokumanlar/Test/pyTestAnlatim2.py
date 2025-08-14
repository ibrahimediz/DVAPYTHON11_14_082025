import unittest
from unittest.mock import patch
from apicall import get_user_data

class TestAPIClient(unittest.TestCase):
    @patch("apicall.requests.get")
    def test_get_user_data(self,mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value={"id":1,"name":"Test user"}

        mock_get.return_value = mock_response

        result = get_user_data(1)

        mock_get.assert_called_once_with("http://api.example.com/users/1")

        self.assertEqual(result,{"id":1,"name":"Test user"})

if __name__ == "__main__":
    unittest.main()