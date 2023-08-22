import os

fname = ''

fPath = 'C:\\A\\'

abPath = os.path.join(fPath, fname)

print(abPath)

print(os.getcwd(abPath))
