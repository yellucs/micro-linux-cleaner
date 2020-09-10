#https://github.com/yellucs/tiny-linux-cleaner/
#Requires Python3
import subprocess
a = 'sudo '
b = 'apt-get '
c = ' && '
d = ' --fix-missing'
e = 'update'
f = 'dpkg --configure -a'
g = 'dist-upgrade -y'
h = 'upgrade -y'
i = 'autoremove -y'
j = 'clean'
cmd = a+b+e+d+c+a+f+c+a+b+g+c+a+b+h+c+a+b+i+c+a+b+j+c+a+b+e
subprocess.run(cmd, shell=True, check=True)
