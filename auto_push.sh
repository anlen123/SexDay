#!/bin/bash
cd /root/SexDay
/root/miniconda3/bin/python3 sex.py
date=$(date +%Y-%m-%d)
git add *
git add -A 
git commit -m "$date"
git status
git push 
touch flag
