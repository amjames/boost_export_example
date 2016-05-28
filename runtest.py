import os
import sys
import fractal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import time

import argparse
@progfile
def mk_picture(manager,
        xlim=[-2.0,0.5],ylim=[-1.25,1.25],
        npoints=1000,
        dpi=2000,
        maxi=1000):

    xmin =xlim[0]
    xmax =xlim[1]
    ymin =ylim[0]
    ymax =ylim[1]
    tstart=time.time()
    raw_d=manager.update(xmin,xmax,ymin,ymax,maxi)
    tend=time.time()
    sum_ops=0
    for each in raw_d:
        sum_ops += each
    flops = (sum_ops/abs(tend-tstart))/1e-9
    del raw_d
    return flops,abs(tstart-tend)


def main():
    nthread=os.environ["OMP_NUM_THREADS"]
    template="{0:<10}{1:<15}{2:<15}{3:<15}{4:<15}\n"
    outfile=open('python_flops_table.txt','w+')
    outfile.write(template.format("threadn","grid size","max iters","Run time(s)", "GFLOP/s"))
    outfile.write("="*(60)+"\n")
    for n in (1,2,3,4,5):
        print "at n ="+str(n)
        for m in (100,10000):
            print "at m = "+ str(m)
            np = n*m
            f10,  t10   = mk_picture(fractal.ImageManager(np,np,'mandelbrot'),npoints=np,xlim=[-2,-1],ylim=[0,1],maxi=10)
            f50,  t50   = mk_picture(fractal.ImageManager(np,np,'mandelbrot'),npoints=np,xlim=[-2,-1],ylim=[0,1],maxi=50)
            f100, t100  = mk_picture(fractal.ImageManager(np,np,'mandelbrot'),npoints=np,xlim=[-2,-1],ylim=[0,1],maxi=100)
            f1000,t1000 = mk_picture(fractal.ImageManager(np,np,'mandelbrot'),npoints=np,xlim=[-2,-1],ylim=[0,1],maxi=1000)
            outfile.write(template.format(nthread,"({},{})".format(np,np),10  ,t10,f10))
            outfile.write(template.format(nthread,"({},{})".format(np,np),50  ,t50,f50))
            outfile.write(template.format(nthread,"({},{})".format(np,np),100 ,t100,f100))
            outfile.write(template.format(nthread,"({},{})".format(np,np),1000,t1000,f1000))
            outfile.flush()
    outfile.close()





if __name__ == "__main__":
    main()




