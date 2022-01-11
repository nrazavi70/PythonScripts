from GitlabSource import *

def name_change(selected_project):
    while True:
        old_gitlab_variable_key = input("Enter current the part you want to change: (Enter b to go back) ")
        if old_gitlab_variable_key == 'b':
            print('\nGoing back to the main menu')
            break
        else:
            new_gitlab_variable_key = input("Enter what you want to change it to: ")
            project_id = find_project(selected_project)
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                temp_key = variables[i]['key'].replace(old_gitlab_variable_key,new_gitlab_variable_key)
                requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':temp_key, 'value':variables[i]['value'], 'protected':'true'})
            print('Done. You can check changes at '+variables_url)
    