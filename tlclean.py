#https://github.com/yellucs/tiny-linux-cleaner/
import subprocess
a = ' && '
b = ' --fix-missing'
c = 'sudo apt-get update'
d = 'sudo dpkg --configure -a'
e = 'sudo apt-get dist-upgrade -y'
f = 'sudo apt-get upgrade -y'
g = 'sudo apt-get autoremove -y'
h = 'sudo apt-get clean'
cmd = c+b+a+d+a+e+a+f+a+g+a+h+a+c

subprocess.run(cmd, shell=True, check=True)
