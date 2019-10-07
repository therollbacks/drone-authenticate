#!/bin/bash
echo "Started creating CSV"
for file in *.BIN;
do
  filename="${file%.*}"
  python pymavlink/tools/mavlogdump.py --planner --format SIM --types SIM "$file" >> csv/"$filename".csv
  echo "created $file"
done
