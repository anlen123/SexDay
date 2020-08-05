#!/bin/env bash
cd /root/SexDay
python3 sex.py

git add *
git add -A 
git commit -m "每日100张色图"
git status
git push 
