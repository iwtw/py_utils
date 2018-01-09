import skimage.io 
import numpy as np
import argparse 
import json
import time


def parse_args():
    parser = argparse.ArgumentParser( description = "calculate mean of a dataset" )
    parser.add_argument("-input",type=str,help="filename list")
    parser.add_argument("-output",type=str)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args() 

    input_list = open( args.input , "r").read().split("\n")
    input_list.pop()
    #for RGB , 3 channels
    mean = np.zeros(3)
    n = len(input_list)
    prev_time = time.time()
    for i in range( n ):
       img = skimage.io.imread( input_list[i] )
       img = np.array(img)
       img = img.reshape((-1,3))
       mean += np.mean( img , axis=0 )
       if( i % 1000 == 999 ):
           temp_time = time.time()
           print( "%.1f%% , %.1f images/s"%(100*i/n, 1000/ (temp_time - prev_time) ) )
           prev_time = temp_time
           
    mean *= 1.0/n
    print(mean)
    with open(args.output,'w') as json_file:
        json_file.write( json.dump(  {"RGB" : mean } ) )
        


