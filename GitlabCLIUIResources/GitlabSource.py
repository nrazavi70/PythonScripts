import requests
import json
from termcolor import colored

gitlab_url = "https://gitlab.ernyka.com"

token = input(colored("Enter token with api_read and api permission: ",'yellow'))
projects_url = gitlab_url+"/api/v4/projects"
projects_page_response = requests.get(projects_url, headers={'PRIVATE-TOKEN':token})
projects = json.loads(projects_page_response.text)

def find_project(selected_project):
    for i in range(len(projects)):
        if str(i+1) == selected_project or projects[i]['name'] == selected_project:
            project_id = projects[i]['id']
            break
        else:
            project_id = None
    if project_id is None:
        print(colored('No such project exists.','red'))
    return project_id
    