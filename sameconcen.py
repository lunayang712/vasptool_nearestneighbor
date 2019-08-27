import os,glob
import numpy as np
from natsort import natsorted
import pandas as pd
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
fc = open ('fc.txt','w')
for folder in folders_all[:]:
    try:
        parameters = folder.split('\\')[-1]
        fc.write("%s"%parameters)
        num = open(folder+'\\CONTCAR','r').readlines()[6]
        #nam,num = open(folder+'\\CONTCAR','r').readlines()[5:6]
        fc.write("%s"%num)
        #numc = open(folder+'\\CONTACR','r').readlines()[6]
        #print(numc)
        #fc.write("%s\n"%numc)
    except FileNotFoundError:
        pass
fc.close()