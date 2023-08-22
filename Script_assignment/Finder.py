
import os,time

##This sets our original absolute path
Dpath='C:\\Users\\theck\\Documents\\Repositories\\GitHub\\Python_Projects\\Python_Projects\\Script_Challenge\\A'
##This saved all the files at the end of our absolute path
files = os.listdir(Dpath)
##This saves the specific files ending in .txt to a list
txt_files=[x for x in files if '.txt' in x]
##This reviews through our list of files and documents the absolute path for each files location.
for i in range(len(txt_files)):
    path = os.path.join(Dpath, str(txt_files[i]))
## this gets us the date and time for modification
    ts = os.path.getmtime(path)
    tp = time.localtime(ts)
    print(txt_files[i] + '- This was last modified: ' + time.strftime('%Y-%m-%d %H:%M:%S', tp))







