import requests
import json

old_gitlab_environment = "value1"
new_gitlab_environment = "value2"

token = input("Enter token with api_read and api permission: ")
projects_url = "https://gitlab.ernyka.com/api/v4/projects"
projects_page_response = requests.get(projects_url, headers={'PRIVATE-TOKEN':token})
projects = json.loads(projects_page_response.text)
def change_var():
        project_name = input("Enter project's name: ")    
        for i in range(len(projects)):
            if projects[i]['name'] == project_name:
                project_id = projects[i]['id']
                break
            else:
                project_id = 'undefined'        
        if project_id == 'undefined':
            print('No such project exists.')
        else:
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                if variables[i]['environment_scope'] == old_gitlab_environment:
                    requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':variables[i]['key'],'value':variables[i]['value'],'environment_scope':new_gitlab_environment, 'protected':'true'})
            print('Done. You can check changes at '+variables_url)
            def continue_choice():
                cont_choice = input("Do you want to continue: (y/n) ")
                if cont_choice == 'y':
                    change_var()
                elif cont_choice == 'n':
                    print('Bye')
                else:
                    print('Please enter a valid response (Y/N , y/n , yes/no)')
                    continue_choice()
            continue_choice()
if projects_page_response.status_code == 401:
    print('Wrong or expired token.')
else:
    change_var()
