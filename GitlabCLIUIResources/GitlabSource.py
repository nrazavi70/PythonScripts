import requests
import json
from termcolor import colored

gitlab_url = input(colored("Enter your gitlab url: ",'yellow'))

token = input(colored("Enter token with api_read and api permission: ",'yellow'))
projects_url = gitlab_url+"/api/v4/projects?per_page=100&page="
projects_page_responses = ""
for i in range(10):
    projects_page_response = requests.get(projects_url+str(i), headers={'PRIVATE-TOKEN':token})
    if projects_page_response.text != "[]":
        projects_page_responses = projects_page_responses + projects_page_response.text
projects_page_responses = projects_page_responses.replace('][{"id',',{"id')
projects = json.loads(projects_page_responses)

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
    