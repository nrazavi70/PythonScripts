from GitlabCLIUIResources.GitlabSource import *

def create_var_with_file(project_id):
    while True:
        variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
        var_file_path = input((colored("\nEnter variable file absolute path: (Enter b to go back.) ",'yellow')))
        if var_file_path == 'b':
            break
        else:
            var_file = open(var_file_path,'r').read()
            if var_file == '':
                print(colored("File is empty or doesn't exist.",'red'))
            else:
                parsed_vars = var_file.split('\n')
                var_env = input(colored("\nEnter variables environment: ",'yellow'))
                for var in parsed_vars:
                    var_key = var.split('=')[0]
                    var_value = var.split('=')[1]
                    requests.post(variables_url, headers={'PRIVATE-TOKEN':token},data={'key':var_key,'value':var_value,'environment_scope':var_env, 'protected':'true'})
                    print(colored("\nKey: "+var_key+'\nValue: '+var_value+"\nEnvironment: "+var_env+"\nhas been created.",'green'))
                print(colored("\nAll variables are added. You can check changes at\n"+variables_url,'green'))
