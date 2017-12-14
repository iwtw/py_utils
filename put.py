import sys
import os
import shutil

dirs = os.listdir(".")
for _,dirname in enumerate(dirs):
    if( dirname == "put.py" ):
        continue
    os.chdir( dirname )
    filenames = os.listdir(".")
    for _,filename in enumerate( filenames ):
        if filename[-4:] != ".png" and filename[-4:] != ".jpg":
            continue
        label = filename.split('/')[-1].split('_')[-2]
        if not os.path.exists( label ):
            os.mkdir( label )
        shutil.move( filename , label )
    os.chdir("..")

