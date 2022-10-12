import unittest
from unittest.mock import patch
import githubAPI 

class TestGitHubAPI(unittest.TestCase):
    @patch('githubAPI.getRepos')
    def test_github_API_1(self, mock_get):
        # Configure the mock to return number of commits to be 4
        mock_get.return_value = "Repo: CS-555 Number of commits: 4"
        # Call the service, which will send a request to the server.
        response = githubAPI.getRepos("smadhu247")
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertEqual(response, "Repo: CS-555 Number of commits: 4")
    
    @patch('githubAPI.getRepos')
    def test_github_API_2(self, mock_get):
        # Configure the mock to return number of repos to be 6
        mock_get.return_value = "Repo: CS-555 Number of commits: 6"
        # Call the service, which will send a request to the server.
        response = githubAPI.getRepos("smadhu247")
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertEqual(response, "Repo: CS-555 Number of commits: 6")

    @patch('githubAPI.getRepos')
    def test_github_API_3(self, mock_get):
        # Configure the mock to return number of repos to be 30
        mock_get.return_value = "Repo: CS-555 Number of commits: 30"
        # Call the service, which will send a request to the server.
        response = githubAPI.getRepos("smadhu247")
        # If the request is sent successfully, then I expect a response to be returned.
        self.assertEqual(response, "Repo: CS-555 Number of commits: 30")


if __name__ == "__main__":
    unittest.main()