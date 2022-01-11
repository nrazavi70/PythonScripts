from GitlabSource import *

def search_var(selected_project):
    while True:
        searched_string = input("Enter the var you are looking for: (Enter b to go back) ")
        if searched_string == 'b':
            print('Going back to the main menu')
            return None
        else:
            project_id = find_project(selected_project)
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                if searched_string in variables[i]['key']:
                    print(str(i+1)+". "+variables[i]['key'])