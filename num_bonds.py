import ase, glob
import ase.io.vasp
import ase.neighborlist
import numpy as np
from natsort import natsorted
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
numb = open ('numbonds.txt','w')
for folder in folders_all[:]:
    atoms=ase.io.vasp.read_vasp(folder+'\\CONTCAR')
#    n1,n2,n3,n4 =number of Mo,S,Se,W
    parameters = folder.split('\\')[-1]
    numb.write("%s "%parameters)
#i,j,k,l,m,n = MoMo,MoW,WW,SS,SeS,SeSe#
    #i=ase.neighborlist.neighbor_list('i',atoms,{('Mo', 'Mo'):4})
    #j=ase.neighborlist.neighbor_list('i',atoms,{ ('Mo', 'W'):4})
    #k=ase.neighborlist.neighbor_list('i',atoms,{('W', 'W'): 4})
    l=ase.neighborlist.neighbor_list('i',atoms,{('S', 'S'):4})
    m=ase.neighborlist.neighbor_list('i',atoms,{('S', 'Se'):4})
    n=ase.neighborlist.neighbor_list('i',atoms,{('Se','Se'):4})
    #print(i,j,k,l,m,n)
    #coord1=np.bincount(i)
    #coord2=np.bincount(j)
    #coord3=np.bincount(k)
    coord4=np.bincount(l)
    coord5=np.bincount(m)
    coord6=np.bincount(n)
    #sum1=0.5*sum(coord1)
    #sum2=0.5*sum(coord2)
    #sum3=0.5*sum(coord3)
    sum4=0.5*sum(coord4)
    sum5=0.5*sum(coord5)
    sum6=0.5*sum(coord6)
#    numb.write("%d %d %d %.1f %.1f %.1f\n"%(sum1,sum2,sum3,sum4,sum5,sum6))
    numb.write("%.1f %.1f %.1f\n"%(sum4,sum5,sum6))
    #print(sum1,sum2,sum3,sum4,sum5,sum6)