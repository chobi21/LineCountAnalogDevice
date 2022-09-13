#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:15:37 2022
@author: rashidahasan
"""

import os

def countlines(directory="./Home", lines=0, filecount=0, ext=".txt", skip_blank=False):
    '''counts the total number of files and lines and  average number of lines for each file'''
    for root, _dirs, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(ext):
                continue
            file = os.path.join(root, filename)
            filecount += 1
            with open(file, "r", encoding="utf-8") as openfile:
                if skip_blank:
                    new_lines = len([i for i in openfile.readlines() if i.strip()])
                else:
                    new_lines = len(openfile.readlines())
                lines = lines + new_lines
            print(file, "------>", new_lines)
    print("................\n")
    print("Total Number of files found", filecount)
    print("Total Number of Lines", lines)
    print("Average lines per file", lines/filecount)
countlines(directory="./HomeADirectory", ext="txt", skip_blank=True)
