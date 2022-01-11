from GitlabSource import *

def list_vars(selected_project):
    print('\nAll of your variables: ')
    project_id = find_project(selected_project)
    variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
    variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
    variables = json.loads(variables_page_response.text)
    for i in range(len(variables)):
        print(str(i+1)+". "+variables[i]['key']+" : "+variables[i]['value'])
    return None