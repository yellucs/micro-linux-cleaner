#! /bin/bash
#https://github.com/yellucs/tiny-linux-cleaner
a='sudo '
b='apt-get '
c=' && '
d=' --fix-missing'
e='update'
f='dpkg --configure -a'
g='dist-upgrade -y'
h='upgrade -y'
i='autoremove -y'
j='clean'
cmd=$a$b$e$d$c$a$f$c$a$b$g$c$a$b$h$c$a$b$i$c$a$b$j$c$a$b$e
output=$(eval "$cmd")
echo "$output"
