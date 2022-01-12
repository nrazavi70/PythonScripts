from GitlabCLIUIResources.GitlabSource import *

def name_change(project_id):
    while True:
        old_gitlab_variable_key = input("\nEnter current the part you want to change: (Enter b to go back) ")
        if old_gitlab_variable_key == 'b':
            print(colored('\nGoing back to the main menu','yellow'))
            break
        else:
            new_gitlab_variable_key = input(colored("Enter what you want to change it to: ",'yellow'))
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                temp_key = variables[i]['key'].replace(old_gitlab_variable_key,new_gitlab_variable_key)
                requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':temp_key, 'value':variables[i]['value'], 'protected':'true'})
            print(colored('Done. You can check changes at '+variables_url,'yellow'))
    