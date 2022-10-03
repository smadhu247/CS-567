import unittest
from githubAPI import getRepos

class TestGithubAPI(unittest.TestCase):

    def testOne(self): 
        self.assertEqual(getRepos("smadhu247"),'Repo: CS-555 Number of commits: 30\nRepo: CS_146 Number of commits: 5\nRepo: hello-world Number of commits: 1\nRepo: TicTacToe Number of commits: 1')
    
    def testTwo(self): 
        self.assertEqual(getRepos("richkempinski"),'Repo: csp Number of commits: 2\nRepo: hellogitworld Number of commits: 2\nRepo: helloworld Number of commits: 2\nRepo: Mocks Number of commits: 2\nRepo: Project1 Number of commits: 2\nRepo: richkempinski.github.io Number of commits: 2\nRepo: threads-of-life Number of commits: 2\nRepo: try_nbdev Number of commits: 2\nRepo: try_nbdev2 Number of commits: 2')

    def testThree(self): 
        self.assertEqual(getRepos("ibdasuhvlinwcjbhvsfv"), 'Username was not found')

    def testFour(self): 
        self.assertNotEqual(getRepos("smadhu247"), 'Username was not found')

    def testFive(self): 
        self.assertNotEqual(getRepos("richkempinski"), 'Username was not found')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
