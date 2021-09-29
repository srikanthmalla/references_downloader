#!/usr/bin/python
# Author Srikanth Malla
# prerequisites: sopaper [https://github.com/ppwwyyxx/SoPaper]
# inputs: references file and output dir path
# outputs: downloaded papers and undownloadable paper names

import os
import subprocess

references_file = "./titan_references.txt"
output_dir = "./downloads/"

non_downloadable = "debug.txt"

file1 = open(references_file, 'r')
Lines = file1.readlines()
for ind, line in enumerate(Lines):
  out_file = output_dir+str(ind+1)+".pdf" #because ind starts from 0
  title = line.split(".")[1]
  test = subprocess.Popen(["sopaper",title,"-o", out_file], stdout=subprocess.PIPE)
  output = test.communicate()[0]
  print(output)
