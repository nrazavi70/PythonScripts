from GitlabCLIUIResources.GitlabSource import *
from tabulate import tabulate

def list_vars(project_id):
    print(colored('\nAll of your variables: ','green'))
    variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
    variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
    variables = json.loads(variables_page_response.text)
    var_table = [['ID','Key','Value','ENV'],['-','-','-','-']]
    for i in range(len(variables)):
        var_table.append([str(i+1),variables[i]['key'],variables[i]['value'],variables[i]['environment_scope']])
        #print(str(i+1)+". "+variables[i]['key']+" : "+variables[i]['value']+" | "+variables[i]['environment_scope'])
    print(tabulate(var_table))
    return None