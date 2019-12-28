import subprocess
a = ' && '
b = 'sudo apt-get update --fix-missing'
c = 'sudo apt-get dist-upgrade -y'
d = 'sudo apt-get upgrade -y'
e = 'sudo apt-get autoremove -y'
f = 'sudo apt-get clean'
command = b+a+c+a+d+a+e+a+f

subprocess.run(command, shell=True, check=True)
