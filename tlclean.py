#https://github.com/yellucs/tiny-linux-cleaner/
import subprocess
a = 'sudo '
b = 'apt-get '
c = ' && '
d = ' --fix-missing'
e = a,b,'update'
f = a'dpkg --configure -a'
g = a,b,'dist-upgrade -y'
h = a,b,'upgrade -y'
i = a,b,'autoremove -y'
j = a,b,'clean'
cmd = e+d+c+f+c+g+c+h+c+i+c+j+c+e

subprocess.run(cmd, shell=True, check=True)
