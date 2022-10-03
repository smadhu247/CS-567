import requests
import json

def getRepos(username):

    repo_names = {}
    return_string = ""
    
    try:
        repos = requests.get('https://api.github.com/users/' + username + '/repos')
    except:
        return "Username was not found"

    for i in range(len(repos.json())):
        repo_name = repos.json()[i]["name"]
        try:
            commits = requests.get('https://api.github.com/repos/' + username + '/' + repo_name + '/commits')
        except:
             return "Username or repo name was not found"
        repo_names[repo_name] = len(commits.json())

    for key, value in repo_names.items():
       return_string = + return_string + "Repo: " + key + " Number of commits: " + str(value) + "\n"

    return return_string

if __name__ == '__main__':        
    getRepos("smadhu247")
    getRepos("richkempinski")