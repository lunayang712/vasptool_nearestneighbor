import numpy as np
import ase, glob, math
import ase.io.vasp
import ase.neighborlist
from natsort import natsorted
#folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
er = open ('newbtypeerrorbonds.txt','w')
#tes = open ('testarray.txt','w')
for folder in folders_all[:]:
#    atoms=ase.io.vasp.read_vasp(folder+'\\CONTCAR')
#    n1,n2,n3,n4 =number of Mo,S,Se,W
    parameters = folder.split('\\')[-1]
    er.write("%s "%parameters)
    num = open(folder+'\\CONTCAR','r').readlines()[6]
#    print(num)
    Mo = int(num.split()[0])
    S = int(num.split()[1])
    Se = int(num.split()[-1])
    print("%d %d %d"%(Mo,S,Se))
#    W = int(num.split()[-1])
#    er.write("%d %d\n"%(S,Se))
    n = S+Se
    m = 3
    a = [[0]*m for i in range(n)]
    for j in range(n):
        pos=open(folder+'\\CONTCAR', 'r').readlines()[8+Mo+j]
#        print(float(pos.split()[1]))
        a[j][0] =float(pos.split()[0])
        a[j][1] =float(pos.split()[1])
        a[j][2] =float(pos.split()[2])
#    print("%s %d %f %f %f"%(parameters,n,a[0][0],a[0][1],a[0][2]))
    ss = 0
    sse = 0
    sese = 0
    for k in range(n-1):
        print("%d"%k)
        q=k+1
        print("%d"%q)
#        ss = 0
#        sse = 0
#        sese = 0
        #        if q=n:
#            break;
        while q<n:
#            if ((math.fabs(a[k][0]-a[q][0]))<=0.1) & ((math.fabs(a[k][1]-a[q][1]))<=0.1) :          
#            if ((math.fabs(a[k][0]-a[q][0])<=0.1) | (math.fabs(a[k][0]-a[q][0])>=0.9))== ((math.fabs(a[k][2]-a[q][2])<=0.1) | (math.fabs(a[k][2]-a[q][2])>=0.9)) == (math.fabs(a[k][1]-a[q][1])>0.00001) == (math.fabs(a[k][1]-a[q][1])<0.9):
#            if (((math.fabs(a[k][0]-a[q][0]))<=0.1) or ((math.fabs(a[k][0]-a[q][0]))>=0.9)) and (((math.fabs(a[k][1]-a[q][1]))<=0.1) or ((math.fabs(a[k][1]-a[q][1]))>=0.9)) and ((math.fabs(a[k][2]-a[q][2]))>0.00001) and ((math.fabs(a[k][2]-a[q][2]))<0.9):
            if (((math.fabs(a[k][0]-a[q][0]))<=0.1) or ((math.fabs(a[k][0]-a[q][0]))>=0.9)) and (((math.fabs(a[k][2]-a[q][2]))<=0.1) or ((math.fabs(a[k][2]-a[q][2]))>=0.9)) and ((math.fabs(a[k][1]-a[q][1]))>0.00001) and ((math.fabs(a[k][1]-a[q][1]))<0.9):
                print("%d %d"%(q,k))

                #            if ((math.fabs(a[k][0]-a[q][0])<=0.01) | (math.fabs(a[k][0]-a[q][0])>=0.99)):
#                print(math.fabs(a[k][0]-a[q][0]))
#                print(math.fabs(a[k][1]-a[q][1]))
#                remember it is q<s not q<=S
                if q<S:
                    ss =ss+1
                    q =q+1
                    print("ss:%d"%ss)
                elif k<=S:
                    sse =sse+1
                    q =q+1
                else:
                    sese =sese+1
                    q =q+1
#            er.write("%d %d %d\n"%(ss,sse,sese))
#                q +=1
#                continue
            else:
                q =q+1
#                continue
#            er.write("%d %d %d\n"%(ss,sse,sese))
#        else:
#            break
        print("%d %d %d "%(ss,sse,sese))
    er.write("%d %d %d\n"%(ss,sse,sese))
#        print(a)
#    S_bin=[]