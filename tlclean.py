import subprocess
a = ' && '
b = 'sudo apt-get update --fix-missing'
c = 'sudo dpkg --configure -a'
d = 'sudo apt-get dist-upgrade -y'
e = 'sudo apt-get upgrade -y'
f = 'sudo apt-get autoremove -y'
g = 'sudo apt-get clean'
cmd = b+a+c+a+d+a+e+a+f+a+g+b

subprocess.run(cmd, shell=True, check=True)
#https://github.com/yellucs/tiny-linux-cleaner/
