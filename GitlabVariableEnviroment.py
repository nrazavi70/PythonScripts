import requests
import json

old_gitlab_environment = "ENV1"
new_gitlab_environment = "ENV2"

token = input("Enter token with api_read and api permission: ")
projects_url = "https://gitlab.ernyka.com/api/v4/projects"
projects_page_response = requests.get(projects_url, headers={'PRIVATE-TOKEN':token})
projects = json.loads(projects_page_response.text)
if projects_page_response.status_code == 401:
    print('Wrong or expired token.')
else:
    while True:
        project_name = input("Enter project's name: (Enter q to exit) ")    
        if project_name == 'q':
            print('Goodbye!')
            break
        else:
            for i in range(len(projects)):
                if projects[i]['name'] == project_name:
                    project_id = projects[i]['id']
                    break
                else:
                    project_id = None    
            if project_id is None:
                print('No such project exists.')
            else:
                variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
                variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
                variables = json.loads(variables_page_response.text)
                for i in range(len(variables)):
                    if variables[i]['environment_scope'] == old_gitlab_environment:
                        requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':variables[i]['key'],'value':variables[i]['value'],'environment_scope':new_gitlab_environment, 'protected':'true'})
                print('Done. You can check changes at '+variables_url)
