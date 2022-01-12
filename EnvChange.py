from GitlabSource import *
from VarOps import var_ops

def env_change(project_id):
    while True:
        old_gitlab_environment = input(colored("Enter current environment of variables: (Enter b to go back) ",'yellow'))
        if old_gitlab_environment == 'b':
            print(colored("\nGoing back to the main menu.",'yellow'))
            break
        else:
            new_gitlab_environment = input(colored("Enter desired environment of variables: ",'yellow'))
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                if variables[i]['environment_scope'] == old_gitlab_environment:
                    requests.post(variables_url, headers={'PRIVATE-TOKEN':token}, data={'key':variables[i]['key'],'value':variables[i]['value'],'environment_scope':new_gitlab_environment, 'protected':'true'})
            print(colored('Done. You can check changes at\n'+variables_url,'green'))
    