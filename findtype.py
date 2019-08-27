import numpy as np
import ase, glob, math
#import ase.io.vasp
#import ase.neighborlist
from natsort import natsorted
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
#folders_all = natsorted(glob.glob('.\\test\\*'))
findtp = open ('findtype.txt','w')
#tes = open ('testarray.txt','w')
for folder in folders_all[:]:
#    atoms=ase.io.vasp.read_vasp(folder+'\\CONTCAR')
#    n1,n2,n3,n4 =number of Mo,S,Se,W
    parameters = folder.split('\\')[-1]
    findtp.write("%s "%parameters)
#    num = open(folder+'\\CONTCAR','r').readlines()[6]
    alength = open(folder+'\\CONTCAR','r').readlines()[2]
    a1=float(alength.split()[0])
    a2=float(alength.split()[1])
    a3=float(alength.split()[2])
    blength = open(folder+'\\CONTCAR','r').readlines()[3]
    b1=float(blength.split()[0])
    b2=float(blength.split()[1])
    b3=float(blength.split()[2])
    clength = open(folder+'\\CONTCAR','r').readlines()[4]
    c1=float(clength.split()[0])
    c2=float(clength.split()[1])
    c3=float(clength.split()[2])
    print("%f %f %f"%(c1,c2,c3))
    if (math.fabs(a1)<=0.1) == (math.fabs(a2)<=0.1) == (math.fabs(a3)>=11.5) == (math.fabs(a3)<=13):
        findtp.write("A\n")
    elif (math.fabs(b1)<=0.1) == (math.fabs(b2)<=0.1) == (math.fabs(b3)>=11.5) == (math.fabs(b3)<=13):
        findtp.write("B\n")
    elif (math.fabs(c1)<=0.1) == (math.fabs(c2)<=0.1) == (math.fabs(c3)>=11.5) == (math.fabs(c3)<=13):
        findtp.write("C\n")      
    else:
        findtp.write("\n")