from GitlabCLIUIResources.GitlabSource import *
from GitlabCLIUIResources.DeleteVar import delete_var
from GitlabCLIUIResources.CreateVar import create_var
from GitlabCLIUIResources.EnvChange import env_change
from GitlabCLIUIResources.ListProjects import list_projects
from GitlabCLIUIResources.NameChange import name_change
from GitlabCLIUIResources.SearchVar import search_var
from GitlabCLIUIResources.ListVars import list_vars

initial_choice = None
selected_project = None
if projects_page_response.status_code == 401:
    print(colored('Wrong or expired token.\n','red'))
else:
    if selected_project is None:
        while True:
            if selected_project == 'q':
                print(colored('\nGoodbye!\n','green'))
                break
            else:
                list_projects()
                selected_project = input(colored("\nEnter project's name or ID: (Enter q to exit) ",'yellow'))
                if selected_project == 'q':
                    print(colored('\nGoodbye!\n','green'))
                    break
                else:
                    project_id = find_project(selected_project)
                    if project_id is None:
                        continue
                    else:
                        
                        while True:
                            if initial_choice is None:
                                list_vars(project_id)
                                print(colored("\nc     ",'yellow'),colored("Create a new variable",'blue'),colored("\
                                               \ns     ",'yellow'),colored("Search for a variable.",'blue'),colored("\
                                               \nd     ",'yellow'),colored("Delete a variable.",'blue'),colored("\
                                               \nce    ",'yellow'),colored("Change variable environment in a project and add new variables with the new environment.",'blue'),colored("\
                                               \ncn    ",'yellow'),colored("Change a part of a variable's name and add new variables with the new name.",'blue'),colored("\
                                               \nb     ",'yellow'),colored("Select another project.",'blue'),colored('\
                                               \nq     ','yellow'),colored("Exit",'blue'))
                                initial_choice = input(colored("\n\nWhat do you want to do? ","yellow"))
                                # initial_choice = input("\nc:     Create a new variable.\
                                                        # \ns:     Search for a variable.\
                                                        # \nd:     Delete a variable.\
                                                        # \nce:    Change variable environment in a project and add new variables with the new environment.\
                                                        # \ncn:    Change a part of a variable's name and add new variables with the new name.\
                                                        # \nb:     Select another project.\
                                                        # \nq:     Exit\
                                                        # \n\nWhat do you want to do? "
                            elif initial_choice == 'b':
                                initial_choice = None
                                selected_project = None
                                break
                            elif initial_choice == 'd':
                                initial_choice = delete_var(project_id)
                            elif initial_choice == 'ce':
                                initial_choice = env_change(project_id)
                            elif initial_choice == 'cn':
                                initial_choice = name_change(project_id)
                            elif initial_choice == 'c':
                                initial_choice = create_var(project_id)
                            elif initial_choice == 's':
                                initial_choice = search_var(project_id)
                            elif initial_choice == 'q':
                                selected_project = 'q'
                                break
                            else:
                                initial_choice = None
                                break