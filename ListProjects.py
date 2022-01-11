from GitlabSource import *

def list_projects():
    print('\nAll of your projects: ')
    for i in range(len(projects)):
        print(str(i+1)+". "+projects[i]['name'])
    return None