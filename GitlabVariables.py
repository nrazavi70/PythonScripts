from GitlabSource import *
from CreateVar import create_var
from EnvChange import env_change
from ListProjects import list_projects
from NameChange import name_change
from SearchVar import search_var
from ListVars import list_vars

initial_choice = None
selected_project = None
if projects_page_response.status_code == 401:
    print('Wrong or expired token.\n')
else:
    while True:
        if selected_project is None:
            list_projects()
            selected_project = input("\nEnter project's name: (Enter q to exit) ")
        if selected_project == 'q':
            print('\nGoodbye!\n')
            break
        else:
            list_vars(selected_project)
            if initial_choice is None:
                initial_choice = input("\nc:     Create a new variable.\
                                        \ns:     Search for a variable.\
                                        \nce:    Change variable environment in a project and add new variables with the new environment.\
                                        \ncn:    Change a part of a variable's name and add new variables with the new name.\
                                        \nb:     Select another project.\
                                        \nq:     Exit\
                                        \n\n What do you want to do? ")
            if initial_choice == 'q':
                print('\nGoodbye!\n')
                break
            elif initial_choice == 'b':
                initial_choice = None
                selected_project = None
                continue
            elif initial_choice == 'ce':
                initial_choice = env_change(selected_project)
            elif initial_choice == 'cn':
                initial_choice = name_change(selected_project)
            elif initial_choice == 'c':
                initial_choice = create_var(selected_project)
            elif initial_choice == 's':
                initial_choice = search_var(selected_project)