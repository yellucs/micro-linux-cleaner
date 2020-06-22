# Tiny Linux Cleaner (TLC)
 Update/Upgrade and clean your Linux pc with this tiny python script.
 This script will perform Linux apt fixes automatically to easily recover from a system crash.
 It will also update repositories, upgrade your packages, and even remove any unused packages. Just by running one python script :)
 
#### Requirments 
   * Python3
```
$ sudo apt-get update
$ sudo apt-get install python3 -y
```

## Download & Run With Git

```
git clone https://github.com/yellucs/tiny-linux-cleaner.git
cd tiny-linux-cleaner
python3 tlclean.py 
```
#### Alternative Download Method

```
$ wget https://github.com/yellucs/tiny-linux-cleaner/raw/master/tlclean.py
$ python3 tlclean.py 
```

## When to use
 Run the script when you would like to update/upgrade/clean your Linux based system. DO NOT set the script to autorun, while it is designed to be automatic it should not be run unattended. The time for TLC to finish depends on your system specifications; internet speed and amount of pending updates. If you encounter any errors re-running the script after it first stops should correct it :)
