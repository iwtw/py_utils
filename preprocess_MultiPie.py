import PIL.Image
import numpy
import skimage
import os
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser( description = "bicubic" )
    parser.add_argument("-input_list")
    parser.add_argument("-output_dir")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parser_args()
    input_list = open(args.input_list,'r').read().split('\n')
    input_list.pop()

    os.system('mkir -p {}'.format(args.output_dir))
    for img_name in tqdm( input_list ):
        img = PIL.Image.open( input_list[i] )
        name = img_name.split('/')[-1]
        img = img.resize( ( 240,320 ) , PIL.Image.LANCZOS )
        img = img.crop( ( (320-128)//2 + 1  , (240-128)//2 + 1 , 320 - (320-128)//2, 240 - (240-128)//2 ) )
        img.save(  args.output_dir + '/' + name) 
