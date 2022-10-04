import unittest
from githubAPI import getRepos

# Standard library imports...
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none

# class TestGithubAPI(unittest.TestCase):

#     def testOne(self): 
#         self.assertEqual(getRepos("smadhu247"),'Repo: CS-555 Number of commits: 30\nRepo: CS_146 Number of commits: 5\nRepo: hello-world Number of commits: 1\nRepo: TicTacToe Number of commits: 1\n')
    
#     def testThree(self): 
#         self.assertEqual(getRepos("ibdasuhvlinwcjbhvsfv"), 'Username was not found')

#     def testFour(self): 
#         self.assertNotEqual(getRepos("smadhu247"), 'Username was not found')

#     def testFive(self): 
#         self.assertNotEqual(getRepos("richkempinski"), 'Username was not found')

# if __name__ == '__main__':
#     print('Running unit tests')
#     unittest.main()

@patch('githubAPI.requests.get')
def test_github_API(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = getRepos("smadhu247")

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
