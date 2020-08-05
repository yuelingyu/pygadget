# -*- coding: utf-8 -*-

# https://github.com/j08lue/pycpt/


import os
import numpy as np
from matplotlib import colors as mcolors

def get_continuous_cmap(hex_list, float_list=None):
    ''' creates and returns a color map that can be used in heat map figures.
        If float_list is not provided, colour map graduates linearly between each color in hex_list.
        If float_list is provided, each color in hex_list is mapped to the respective location in float_list. 
        
        Parameters
        ----------
        hex_list: list of hex code strings
        float_list: list of floats between 0 and 1, same length as hex_list. Must start with 0 and end with 1.
        
        Returns
        ----------
        colour map'''
    rgb_list = [rgb_to_dec(hex_to_rgb(i)) for i in hex_list]
    if float_list:
        pass
    else:
        float_list = list(np.linspace(0,1,len(rgb_list)))
        
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp

def hex_to_rgb(value):
    '''
    Converts hex to rgb colours
    value: string of 6 characters representing a hex colour.
    Returns: list length 3 of RGB values'''
    value = value.strip("#") # removes hash symbol if present
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_dec(value):
    '''
    Converts rgb to decimal colours (i.e. divides each value by 256)
    value: list (length 3) of RGB values
    Returns: list (length 3) of decimal values'''
    return [v/256 for v in value]


def export_cmap_to_cpt(cmap, vmin=0,vmax=1, N=255, filename="color_name.cpt",**kwargs):
    # create string for upper, lower colors
    b = np.array(kwargs.get("B", cmap(0.)))
    f = np.array(kwargs.get("F", cmap(1.)))
    na = np.array(kwargs.get("N", (0,0,0))).astype(float)
    ext = (np.c_[b[:3],f[:3],na[:3]].T*255).astype(int)
    extstr = "B {:3d} {:3d} {:3d}\nF {:3d} {:3d} {:3d}\nN {:3d} {:3d} {:3d}"
    ex = extstr.format(*list(ext.flatten()))
    #create colormap
    cols = (cmap(np.linspace(0.,1.,N))[:,:3]*255).astype(int)
    vals = np.linspace(vmin,vmax,N)
    arr = np.c_[vals[:-1],cols[:-1],vals[1:],cols[1:]]
    # save to file
    fmt = "%e %3d %3d %3d %e %3d %3d %3d"
    np.savetxt(filename, arr, fmt=fmt, 
               header="# COLOR_MODEL = RGB",
               footer = ex, comments="")

def gmt_color_map_openfile(cptf, name=None):
    """Read a GMT color map from an OPEN cpt file
    Parameters
    ----------
    cptf : open file or url handle
        path to .cpt file
    name : str, optional
        name for color map
        if not provided, the file name will be used
    """
    # generate cmap name
    if name is None:
        name = '_'.join(os.path.basename(cptf.name).split('.')[:-1])

    # process file
    x = []
    r = []
    g = []
    b = []
    lastls = None
    for l in cptf.readlines():
        ls = l.split()

        # skip empty lines
        if not ls:
            continue

        # parse header info
        if ls[0] in ["#", b"#"]:
            if ls[-1] in ["HSV", b"HSV"]:
                colorModel = "HSV"
            else:
                colorModel = "RGB"
            continue

        # skip BFN info
        if ls[0] in ["B", b"B", "F", b"F", "N", b"N"]:
            continue

        # parse color vectors
        x.append(float(ls[0]))
        r.append(float(ls[1]))
        g.append(float(ls[2]))
        b.append(float(ls[3]))

        # save last row
        lastls = ls

    x.append(float(lastls[4]))
    r.append(float(lastls[5]))
    g.append(float(lastls[6]))
    b.append(float(lastls[7]))
    
    x = np.array(x)
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)

    if colorModel == "HSV":
        for i in range(r.shape[0]):
            # convert HSV to RGB
            rr,gg,bb = colorsys.hsv_to_rgb(r[i]/360., g[i], b[i])
            r[i] = rr ; g[i] = gg ; b[i] = bb
    elif colorModel == "RGB":
        r /= 255.
        g /= 255.
        b /= 255.

    red = []
    blue = []
    green = []
    xNorm = (x - x[0])/(x[-1] - x[0])
    for i in range(len(x)):
        red.append([xNorm[i],r[i],r[i]])
        green.append([xNorm[i],g[i],g[i]])
        blue.append([xNorm[i],b[i],b[i]])

    # return colormap
    cdict = dict(red=red,green=green,blue=blue)
    return mcolors.LinearSegmentedColormap(name=name,segmentdata=cdict)

def gmt_color_map(cptfile, name=None):
    """Read a GMT color map from a cpt file
    Parameters
    ----------
    cptfile : str or open file-like object
        path to .cpt file
    name : str, optional
        name for color map
        if not provided, the file name will be used
    """
    with open(cptfile, 'r') as cptf:
        return gmt_color_map_openfile(cptf, name=name)