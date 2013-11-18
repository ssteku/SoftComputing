#!/bin/bash
python TestResults/Results/resultsGraphs.py
python clasifyNet.py
FILES=./*
cd Charts
rm -rf Converted
mkdir Converted
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  inkscape -z -w 1600 -h 1200 -e Converted/$f.png $f
done