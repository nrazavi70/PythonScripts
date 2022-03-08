from GitlabCLIUIResources.GitlabSource import *
from tabulate import tabulate

def list_projects():
    proj_table = [['ID','Name'],['-','-']]
    print(colored('\nAll of your projects: ','green'))
    for i in range(len(projects)):
        proj_table.append([str(i+1),projects[i]['name']])
        
    print(tabulate(proj_table))
    return None