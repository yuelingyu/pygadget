# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:01:18 2023

@author: yuelingyu
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cmtool


gpf_filename = "temperature.gpf"
cmap_name = "temp_cool"


rgb_data = np.loadtxt(gpf_filename)[:,1:]

hex_list = [ matplotlib.colors.to_hex(rgb_data[i,:]) for i in range(np.shape(rgb_data)[0])  ]
hex_list_r = hex_list[::-1]

mycolor_cmap = cmtool.get_continuous_cmap(hex_list)
mycolor_cmap_r = cmtool.get_continuous_cmap(hex_list_r)


cmtool.export_cmap_to_cpt(mycolor_cmap, vmin=0,vmax=1, N=255 ,filename =  cmap_name + ".cpt")
cmtool.export_cmap_to_cpt(mycolor_cmap_r, vmin=0,vmax=1, N=255 , filename = cmap_name + "_r.cpt")


myColor = cmtool.gmt_color_map(cmap_name + '.cpt')
# myColor = cmtool.gmt_color_map('temperature.cpt')
cs = plt.imshow(np.random.rand(50,50), cmap = myColor)

cbar = plt.colorbar(cs)