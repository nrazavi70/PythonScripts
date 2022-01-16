from GitlabCLIUIResources.GitlabSource import *
from GitlabCLIUIResources.VarOps import var_ops

def delete_var(project_id):
    while True:
            var_number_list = input(colored("\nEnter variable keys or IDs (comma-seperated): (Enter b to go back.) ",'yellow')).split(',')
            if var_number_list[0] == 'b':
                break
            else:
                var_env = input(colored("Enter environment of the var: ",'yellow'))
                var_key_list = []
                for var_number in var_number_list:
                    if var_number is None:
                        print(colored("The var(s) doesn't exist.",'red'))
                        break
                    else:
                        var_key_object = var_ops.key_to_id(project_id,var_number.replace(" ",""))
                        if var_key_object is None:
                            break
                        else:
                            var_key_list.append(var_key_object['key'])
                            delete_confirm = input(colored("This will delete the variable . Are you sure? (y/n) ",'yellow'))
                for var_key in var_key_list:
                    variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables/"+var_key+"?filter[environment_scope]="+var_env
                    var_id = var_ops.key_to_id(project_id,var_key)
                    var_value = var_ops.id_to_value(project_id,var_id)
                    if delete_confirm == 'y':
                        requests.delete(variables_url, headers={'PRIVATE-TOKEN':token})
                        print(colored("\nDone. \nKey: "+var_key+'\nValue: '+var_value+"\nEnvironment: "+var_env+"\nhas been deleted.",'green'))
                        continue
                    elif delete_confirm == 'n':
                        break
