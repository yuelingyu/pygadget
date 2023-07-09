# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:20:33 2023

@author: yuelingyu
"""

import glob
import os
from PIL import Image
import PyPDF2

def combine_img2pdf(folder_path, pdf_name):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            pdf_path = os.path.join(folder_path, filename[:-4] + '.pdf')
            img.save(pdf_path, 'PDF', resolution=100.0)
    
    pdf_merger = PyPDF2.PdfMerger()
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            pdf_merger.append(pdf_path)
    pdf_merger.write(os.path.join(folder_path, pdf_name))
    pdf_merger.close()
    
file_path = os.getcwd()

for glob_dir in glob.glob(file_path + "/*/", recursive = False):
    for dir_path in glob.glob(glob_dir + "/*/", recursive = False):
        print("Starting: ", dir_path, "...")
        print()
        dir_name = os.path.dirname(dir_path)
        pdf_name = os.path.basename(dir_name) + '.pdf'
        with open(pdf_name,"wb") as f:
            combine_img2pdf(dir_path, os.path.join(dir_path, pdf_name))
        for filename in glob.glob(dir_path + "/IMG_*pdf"):
            print(filename)
            os.remove(filename) 


# with open("name.pdf","wb") as f:
#     f.write(img2pdf.convert(glob.glob("/path/to/*.jpg")))
    
    