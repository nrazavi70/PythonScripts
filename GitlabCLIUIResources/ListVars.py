from GitlabCLIUIResources.GitlabSource import *
from tabulate import tabulate

def list_vars(project_id):
    print(colored('\nAll of your variables: ','green'))
    variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
    variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
    if variables_page_response.status_code == 403:
        print(colored('You do not have sufficient permissions on this project.\n','red'))
        return False
    else:
        variables = json.loads(variables_page_response.text)
        var_table = [['ID','Key','Value','ENV'],['-','-','-','-']]
        for i in range(len(variables)):
            var_table.append([str(i+1),variables[i]['key'],variables[i]['value'],variables[i]['environment_scope']])
            #print(str(i+1)+". "+variables[i]['key']+" : "+variables[i]['value']+" | "+variables[i]['environment_scope'])
        print(tabulate(var_table))
        return True