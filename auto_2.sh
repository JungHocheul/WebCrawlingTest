#!/bin/bash

git add .
git commit -m "test commit"
git branch -M main
git remote add origin https://github.com/JungHocheul/WebCrawlingTest.git
git push -u origin main

value=$(<./../email.txt)
echo "$value"

value2=$(<./../token.txt)
echo "$value2"
