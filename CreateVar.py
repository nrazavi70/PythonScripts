from GitlabSource import *

def create_var(selected_project):
    while True:
            project_id = find_project(selected_project)
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            var_key = input("Enter variable key: (Enter b to go back.) ")
            if var_key == 'b':
                break
            else:
                var_value = input("Enter variable value: ")
                var_env = input("Enter variable env: ")
                requests.post(variables_url, headers={'PRIVATE-TOKEN':token},data={'key':var_key,'value':var_value,'environment_scope':var_env, 'protected':'true'})
    