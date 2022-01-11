import requests
import json

token = input("Enter token with api_read and api permission: ")
projects_url = "https://gitlab.ernyka.com/api/v4/projects"
projects_page_response = requests.get(projects_url, headers={'PRIVATE-TOKEN':token})
projects = json.loads(projects_page_response.text)

def find_project(selected_project):
    for i in range(len(projects)):
        if str(i+1) == selected_project or projects[i]['name'] == selected_project:
            project_id = projects[i]['id']
            break
        else:
            project_id = None
    if selected_project is None:
        print('No such project exists.')
    else:
        return project_id