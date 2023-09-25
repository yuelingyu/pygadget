# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:48:42 2023

@author: yuelingyu
"""

import glob, os, shutil

source_dir = os.path.dirname(os.path.realpath(__file__))
# dir_path = os.path.dirname(os.path.realpath(__file__))
dest_dir = os.path.join(source_dir, "new")

for file_name in os.listdir(source_dir):
    
    files = glob.iglob(os.path.join(source_dir,file_name, "*.pdf"))
    
    
    
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, dest_dir)