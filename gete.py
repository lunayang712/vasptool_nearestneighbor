import os,glob
import numpy as np
from natsort import natsorted
#import matplotlib.pyplot as plt
#results = pd.DataFrame()
#folders_all = glob.glob('.\\test2.Mo1_xWxS2\\*')
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
#folders_all = glob.glob('.\\test2.Mo1_xWxS2\\1')
#print(folders_all)
fE=open('quareng.txt','w')
for folder in folders_all:
    parameters = folder.split('\\')[-1]
    fE.write('%s '%parameters)
    #try:
    for line in open(folder+'\\OUTCAR','r').readlines():
        if line.find('TOTEN')>=0:
            toten=float(line.split()[-2])
    fE.write('%f\n'%toten)
            #print(tailer.tail(open('energy12.txt',1)))
            #print(f)
    #except FileNotFoundError:
     #   pass
fE.close()
    #print(toten)
    #energy = pd.read_csv(
           # folder + 'OUTCAR',
    #E = open ("energy.txt","a")
    #E.write('number=%d'%folder,)
    #                     )
    #print(parameters)