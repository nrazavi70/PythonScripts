from GitlabCLIUIResources.GitlabSource import *

class var_ops():
    def key_to_id(project_id,selected_variable_key):
        variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
        variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
        variables = json.loads(variables_page_response.text)
        for i in range(len(variables)):
            if str(i+1) == selected_variable_key or variables[i]['key'] == selected_variable_key:
                variable_id = variables[i]
                break
            else:
                variable_id = None
        if variable_id is None:
            print(colored('No such variable exists','red'))
            return None
        else:
            return variable_id

    def id_to_key(project_id,selected_variable_id):
        variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
        variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
        variables = json.loads(variables_page_response.text)
        for i in range(len(variables)):
            if variables[i] == selected_variable_id:
                variable_key = variables[i]['key']
                break
            else:
                variable_key = None
        if variable_key is None:
            print(colored('No such variable exists','red'))
        else:
            return variable_key

    def id_to_value(project_id,selected_variable_id):
        variables_url = gitlab_url+"/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
        variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
        variables = json.loads(variables_page_response.text)
        for i in range(len(variables)):
            if variables[i] == selected_variable_id:
                variable_value = variables[i]['value']
                break
            else:
                variable_value = None
        if variable_value is None:
            print(colored('No such variable exists','red'))
        else:
            return variable_value