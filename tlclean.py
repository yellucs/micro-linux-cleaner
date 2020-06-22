#https://github.com/yellucs/tiny-linux-cleaner/
import subprocess
a = 'sudo '
b = ' && '
c = ' --fix-missing'
d = a'apt-get update'
e = a'dpkg --configure -a'
f = a'apt-get dist-upgrade -y'
g = a'apt-get upgrade -y'
h = a'apt-get autoremove -y'
i = a'apt-get clean'
cmd = d+c+b+a+e+a+f+a+g+a+h+a+i+d

subprocess.run(cmd, shell=True, check=True)
