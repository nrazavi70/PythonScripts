from GitlabSource import *

def env_change(selected_project):
    while True:
        old_gitlab_environment = input("Enter current environment of variables: (Enter b to go back) ")
        if old_gitlab_environment == 'b':
            print("Going back to the main menu.")
            break
        else:
            new_gitlab_environment = input("Enter desired environment of variables: ")
            project_id = find_project(selected_project)
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                if variables[i]['environment_scope'] == old_gitlab_environment:
                    requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':variables[i]['key'],'value':variables[i]['value'],'environment_scope':new_gitlab_environment, 'protected':'true'})
            print('Done. You can check changes at '+variables_url)
    