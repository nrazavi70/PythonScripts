from GitlabCLIUIResources.GitlabSource import *

def create_var(project_id):
    while True:
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            var_key = input((colored("Enter variable key: (Enter b to go back.) ",'yellow')))
            if var_key == 'b':
                break
            else:
                var_value = input(colored("Enter variable value: "))
                var_env = input(colored("Enter variable env: "))
                requests.post(variables_url, headers={'PRIVATE-TOKEN':token},data={'key':var_key,'value':var_value,'environment_scope':var_env, 'protected':'true'})
                print(colored("Done. "+var_key+" : "+var_value+" has been created. You can check changes at\n"+variables_url,'green'))
    