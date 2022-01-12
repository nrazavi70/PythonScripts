from GitlabSource import *
from tabulate import tabulate

def list_projects():
    proj_table = [['ID','Name','Access-Level'],['-','-','-']]
    print(colored('\nAll of your projects: ','green'))
    for i in range(len(projects)):
        if projects[i]['permissions']['project_access'] is None:
            proj_table.append([str(i+1),projects[i]['name'],projects[i]['permissions']['group_access']['access_level']])
        else:
            proj_table.append([str(i+1),projects[i]['name'],projects[i]['permissions']['project_access']['access_level']])
        #print(str(i+1)+". "+projects[i]['name'])
    print(tabulate(proj_table))
    return None