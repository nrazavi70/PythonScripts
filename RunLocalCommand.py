import subprocess
import shlex
import datetime

command_line = 'sysctl fs.file-nr'
args = shlex.split(command_line)
print('------------------------')
print(datetime.datetime.now())
p = subprocess.run(args)
print('------------------------')
