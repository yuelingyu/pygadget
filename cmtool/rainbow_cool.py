# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:43:45 2020

@author: lingyu.yue
"""


import numpy as np
import matplotlib.pyplot as plt
import cmtool

hex_list = ['#d12325','#f16c2c', '#faad1c', '#f4e313',  '#83c44b', '#61c183', '#13a7b4', '#4066af', '#4a62ac','#7a288a']
hex_list_r = hex_list[::-1]

rainbow_cool = cmtool.get_continuous_cmap(hex_list)
rainbow_cool_r = cmtool.get_continuous_cmap(hex_list_r)


cmtool.export_cmap_to_cpt(rainbow_cool, vmin=0,vmax=1, N=255 ,filename = "rainbow_cool.cpt")
cmtool.export_cmap_to_cpt(rainbow_cool_r, vmin=0,vmax=1, N=255 , filename = "rainbow_cool_r.cpt")


myColor = cmtool.gmt_color_map('rainbow_cool_r.cpt')
cs = plt.imshow(np.random.rand(50,50), cmap = myColor)

cbar = plt.colorbar(cs)