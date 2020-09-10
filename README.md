# Tiny Linux Cleaner (TLC)
 At the flick of a switch this tiny script will update, upgrade, optimise and clean your Linux based PC!
 TLC will perform Linux apt fixes automatically. Use it to easily recover from a system crash.
 
#### Requirments For Python Version
   * Python3
```
$ sudo apt-get update
$ sudo apt-get install python3 -y
```

## Download & Run Python Version Using Git

```
$ git clone https://github.com/yellucs/tiny-linux-cleaner.git
$ cd tiny-linux-cleaner
$ python3 tlclean.py 
```
### Shell Script Version 
```
$ git clone https://github.com/yellucs/tiny-linux-cleaner.git
$ cd tiny-linux-cleaner
$ sudo chmod +x tlclean.sh
$ ./tlclean.sh
```

#### Alternative Download Method

```
$ wget https://github.com/yellucs/tiny-linux-cleaner/raw/master/tlclean.py
$ python3 tlclean.py 
```
#####
```
$ wget https://github.com/yellucs/tiny-linux-cleaner/raw/master/tlclean.sh
$ sudo chmod +x tlclean.sh
$ ./tlclean.sh
```
## When to use
   * Run the script when you would like to update/upgrade/clean your Linux based system. 
   * When your system has crashed during an update

### Cautions
DO NOT set the script to autorun, while it is designed to be automatic it should not be run unattended. The time for TLC to finish depends on your system specifications; internet speed and amount of pending updates. If you encounter any errors re-running the script after it first stops should correct it :)
