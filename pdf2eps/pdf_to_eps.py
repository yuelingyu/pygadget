#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:23:33 2021

@author: lyue
"""

import os
from subprocess import call



def pdf2eps(pdf_dir, eps_dir):
    if not os.path.exists(eps_dir):
        os.mkdir(eps_dir)
    
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            file_name = os.path.splitext(file)[0]
            call(["pdf2ps", file, os.path.join(eps_dir, file_name + ".eps")])
            print(file_name + ".eps", "was generated successfully.")
    return


if __name__ == "__main__":
   pdf_dir = os.getcwd()
   eps_dir = os.path.join(pdf_dir, "files_eps")
   
   pdf2eps(pdf_dir, eps_dir)
        