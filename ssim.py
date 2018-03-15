import numpy as np
import skimage.io
import skimage.measure
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description="calculate PSNR given two list")
    parser.add_argument( '-input_list',type=str,help="receive two arguments , seperated by comma" )
    parser.add_argument( '-range' , type =float , help="the maximum_value - minimum_value , for example 255" )
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()
    list1_name , list2_name = args.input_list.split(',')
    list1 = open( list1_name,"r").read().split('\n')
    list2 = open( list2_name,"r").read().split('\n')
    list1.pop()
    list2.pop()
    assert len(list1) == len(list2)
    ssim = 0 
    n = len(list1)
    a = 1.0/float(n)
    for i in tqdm(range( n)):
        img1 = skimage.io.imread( list1[i])
        img2 = skimage.io.imread( list2[i])
        mse = np.mean( (img1 - img2)**2 )
        ssim += a * skimage.measure.compare_ssim( img1 , img2 , data_range = args.range , multichannel = True   )
    print( ssim )

    
