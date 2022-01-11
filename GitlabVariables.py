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
        list_projects()
        if selected_project is None:
            selected_project = input("Enter project's name: (Enter q to exit) ")
        if selected_project == 'q':
            print('Goodbye!\n')
            break
        else:
            list_vars(selected_project)
            if initial_choice is None:
                initial_choice = input("\nc: Create a new variable.\
                                        \ns: Search for a variable.\
                                        \nce&a: Change variable environment in a project and add new variables with the new environment.\
                                        \ncn&a: Change a part of a variable's name and add new variables with the new name.\
                                        \nb : Select another project.\
                                        \nq: Exit\
                                        \n\n What do you want to do?\n")
            if initial_choice == 'q':
                print('Goodbye!\n')
                break
            elif initial_choice == 'b':
                initial_choice = None
                selected_project = None
                continue
            elif initial_choice == 'ce&a':
                initial_choice = env_change(selected_project)
            elif initial_choice == 'cn&a':
                initial_choice = name_change(selected_project)
            elif initial_choice == 'c':
                initial_choice = create_var(selected_project)
            elif initial_choice == 's':
                initial_choice = search_var(selected_project)