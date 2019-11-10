import subprocess

bashCommand = "ls /"
output = subprocess.check_output(['bash','-c', bashCommand])

print(output)