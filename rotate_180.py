import PIL.Image
import argparse
import os
from tqdm import tqdm

#BATCH_SIZE = 64 
def parse_args():
    parser = argparse.ArgumentParser( description = "rotate_180degree" )
    parser.add_argument("-input_list")
    parser.add_argument("-output_dir")
    flag_parser = parser.add_mutually_exclusive_group(required=False)#whether the input images are in the format of label1/img1 label2/img2
    flag_parser.add_argument("--folder",dest='folder',action="store_true")
    flag_parser.add_argument("--nofolder",dest='folder',action='store_false')
    parser.set_defaults( folder= True )
    args = parser.parse_args()
    return args
def init_dir(d):
    
    l = d.split('/')
    temp = ""
    if not l[0] == "":
        temp += "."

    for i in range(len(l)):
        if l[i] == "":
            continue
        temp +="/" + l[i]
        if not os.path.exists(temp):
            os.mkdir(temp)


if __name__ == "__main__":

    args = parse_args()
    init_dir(args.output_dir)
    print(args.output_dir)

    input_list = open( args.input_list, "r" ).read().split("\n")
    len = len(input_list) - 1 
    t = PIL.Image.open( input_list[0])
    input_height , input_width = t.size
    for i in tqdm(range ( len )):
       # for j in range( np.min( [ len -  i * BATCH_SIZE , BATCH_SIZE ] ) ):
        img = PIL.Image.open(input_list[i])
        t = input_list[i].split('/')
        if args.folder:
            name = t[-2] + '/' + t[-1]
            if not os.path.exists(args.output_dir + "/" + t[-2]):
                os.mkdir(args.output_dir + "/" + t[-2])
        else:
            name = t[-1]
        img.transpose(  PIL.Image.ROTATE_180 )
        img.save( args.output_dir + "/" + name )
