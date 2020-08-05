#!/bin/env bash
cd /root/SexDay
python3 sex.py

/usr/git/bin/git add *
/usr/git/bin/git add -A 
/usr/git/bin/git commit -m "每日100张色图"
/usr/git/bin/git status
/usr/git/bin/git push origin master
