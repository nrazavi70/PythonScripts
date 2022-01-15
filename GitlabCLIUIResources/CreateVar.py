from GitlabCLIUIResources.GitlabSource import *

def create_var(project_id):
    while True:
        variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
        var_key = input((colored("\nEnter variable key: (Enter b to go back.) ",'yellow')))
        if var_key == 'b':
            break
        else:
            var_value = input(colored("Enter variable value: ",'yellow'))
            var_env = input(colored("Enter variable env: ",'yellow'))
            requests.post(variables_url, headers={'PRIVATE-TOKEN':token},data={'key':var_key,'value':var_value,'environment_scope':var_env, 'protected':'true'})
            print(colored("Done. \nKey: "+var_key+'\nValue: '+var_value+"\nEnvironment: "+var_env+"\nhas been created. You can check changes at\n"+variables_url,'green'))
    