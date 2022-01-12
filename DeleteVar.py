from GitlabSource import *
from VarOps import var_ops

def delete_var(project_id):
    while True:
            var_key = input(colored("\nEnter variable key or ID: (Enter b to go back.) ",'yellow'))
            if var_key == 'b':
                break
            else:
                while True:
                    var_env = input(colored("Enter environment of the var: ",'yellow'))
                    var_id = var_ops.key_to_id(project_id,var_key)
                    if var_id is None:
                        break
                    else:
                        var_key = var_ops.id_to_key(project_id,var_id)
                        var_value = var_ops.id_to_value(project_id,var_id)
                        variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables/"+var_key+"?filter[environment_scope]="+var_env
                        delete_confirm = input(colored("This will delete the variable "+var_key+". Are you sure? (y/n) ",'yellow'))
                        if delete_confirm == 'y':
                            requests.delete(variables_url, headers={'PRIVATE-TOKEN':token})
                            print(colored("Done. "+var_key+' : '+var_value+" has been deleted.",'green'))
                            break
                        elif delete_confirm == 'n':
                            break
