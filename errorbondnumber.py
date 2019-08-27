import numpy as np
import ase, glob, math
import ase.io.vasp
import ase.neighborlist
from natsort import natsorted
#folders_all = natsorted(glob.glob('.\\Mo_1_x_W_x_Se_1_x_S_x\\*'))
folders_all = natsorted(glob.glob('.\\MoSeS\\*'))
er = open ('errorbonds.txt','w')
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
#    Se = int(num.split()[-2])
#    W = int(num.split()[-1])
#    er.write("%d %d %d\n"%(Mo,S,Se))
    n = S+Se
    m = 3
    a = [[0]*m for i in range(n)]
    for j in range(n):
        pos=open(folder+'\\CONTCAR', 'r').readlines()[8+Mo+j]
#        print(float(pos.split()[1]))
        a[j][0] =float(pos.split()[0])
        a[j][1] =float(pos.split()[1])
        a[j][2] =float(pos.split()[2])
    for k in range(n-1):
        q=k+1
        ss=0
        sse=0
        sese=0
        #        if q=n:
#            break;
        if q<=n:
            if math.fabs(a[k][0]-a[q][0])<=0.1 == math.fabs(a[k][1]-a[q][1])<=0.1 == math.fabs(a[k][2]-a[q][2])>=0.1 == math.fabs(a[k][2]-a[q][2])<1:
                if q<=S:
                    ss +=1
                    q +=1
                elif k<=S:
                    sse +=1
                    q +=1
                else:
                    sese +=1
                    q +=1
#            er.write("%d %d %d\n"%(ss,sse,sese))
            else:
                q +=1
#            er.write("%d %d %d\n"%(ss,sse,sese))
        else:
            break
        er.write("%d %d %d\n"%(ss,sse,sese))
#        print(a)
#    S_bin=[]