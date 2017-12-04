import PIL.Image
import argparse
import os

#BATCH_SIZE = 64 
def parse_args():
    parser = argparse.ArgumentParser( description = "bicubic" )
    parser.add_argument("-input_list")
    parser.add_argument("-output_dir")
    parser.add_argument("-height",type=int ,help="output_height")
    parser.add_argument("-width",type = int , help="output_width")
    args = parser.parse_args()
    if args.output_dir[-1] != "/":
        args.output_dir += "/"
    return args
def init_dir(d):
    
    l = d.split('/')
    temp = "."
    for i in range(len(l)):
        temp +="/" + l[i]
        if not os.path.exists(temp):
            os.mkdir(temp)


if __name__ == "__main__":

    args = parse_args()
    init_dir(args.output_dir)

    input_list = open( args.input_list, "r" ).read().split("\n")
    len = len(input_list) - 1 
    t = PIL.Image.open( input_list[0])
    input_height , input_width = t.size
    for i in range ( len ):
       # for j in range( np.min( [ len -  i * BATCH_SIZE , BATCH_SIZE ] ) ):
        img = PIL.Image.open(input_list[i])
        t = input_list[i].split('/')
        name = t[-2] + '/' + t[-1]
        if not os.path.exists(args.output_dir + t[-2]):
            os.mkdir(args.output_dir + t[-2])
        img.resize( ( args.width , args.height ) , PIL.Image.BICUBIC ).save( args.output_dir + name )
        
        if i % 10000 == 0 :
            print("%.2f"%(i/len * 100) + "%")
