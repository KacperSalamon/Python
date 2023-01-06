import unittest
from unittest.mock import patch
import requests

def get_user_name(user_id):
  response = requests.get(f'https://api.example.com/users/{user_id}')
  return response.json()['name']

class TestGetUserName(unittest.TestCase):

  @patch('requests.get')
  def test_get_user_name(self, mock_get):
    mock_get.return_value.json.return_value = {'name': 'John Doe'}
    result = get_user_name(1)
    self.assertEqual(result, 'John Doe')

if __name__ == '__main__':
  unittest.main()
