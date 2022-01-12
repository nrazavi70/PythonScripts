from GitlabCLIUIResources.GitlabSource import *

def search_var(project_id):
    while True:
        searched_string = input(colored("Enter the var you are looking for: (Enter b to go back) ",'yellow'))
        if searched_string == 'b':
            print(colored('\nGoing back to the main menu','yellow'))
            return None
        else:
            variables_url = "https://gitlab.ernyka.com/api/v4/projects/"+str(project_id)+"/variables?per_page=100"
            variables_page_response = requests.get(variables_url, headers={'PRIVATE-TOKEN':token})
            variables = json.loads(variables_page_response.text)
            for i in range(len(variables)):
                if searched_string in variables[i]['key']:
                    print(str(i+1)+". "+variables[i]['key'])