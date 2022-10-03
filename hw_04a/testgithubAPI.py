import unittest
from githubAPI import getRepos

class TestGithubAPI(unittest.TestCase):

    def testOne(self): 
        self.assertEqual(getRepos("smadhu247"),'Repo: CS-555 Number of commits: 30\nRepo: CS_146 Number of commits: 5\nRepo: hello-world Number of commits: 1\nRepo: TicTacToe Number of commits: 1\n')
    
    def testThree(self): 
        self.assertEqual(getRepos("ibdasuhvlinwcjbhvsfv"), 'Username was not found')

    def testFour(self): 
        self.assertNotEqual(getRepos("smadhu247"), 'Username was not found')

    def testFive(self): 
        self.assertNotEqual(getRepos("richkempinski"), 'Username was not found')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
