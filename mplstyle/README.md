Customize matplotlib style

1. Check the matplotlib configuration folder ``` matplotlib.get_configdir()```
2. Create the folder ``` stylelib``` if it doesn't exist in matplotlib configureation folder
3. Create or copy the ```mystyle.mplstyle``` files
4. Use customized style by ```plt.style.use('mystyle')```
5. Update if mplstyle file has been modified ``` plt.style.reload_library()```


The details of mplstyle file can be found in https://matplotlib.org/stable/tutorials/introductory/customizing.html
