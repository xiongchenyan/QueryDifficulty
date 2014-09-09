'''
Created on Sep 9, 2014
read all query difficulty splits predictions
get their avg score

read evaluation metrics for Lm baseline
calc pearson, and output
@author: cx
'''

import site
site.addsitedir('/bos/usr0/cx/PyCode/Geektools')
site.addsitedir('/bos/usr0/cx/PyCode/cxPyLib')
site.addsitedir('/bos/usr0/cx/PyCode/QueryDifficulty')
from ResultAnalysis.PearsonCoefficient import *
from QueryDifficultyBasic.QueryDifficultyBase import *
from AdhocEva.AdhocMeasure import *
import os

def LoadAllQueryDifficulty(InDir):
    lTargetDir = []
    for dirname,dirnames,filenames in os.walk(InDir):
        for d in dirnames:
            lTargetDir.append(dirname + "/" + d)
    
    lQD = []
    lName = []
    for Dir in lTargetDir:
        print "reading qd from [%s]" %(Dir)
        lQD.append(QueryDifficultyBaseC(Dir))
        lName.append(Dir)
        
    AvgQD = QueryDifficultyBaseC.Avg(lQD)
    lQD.append(AvgQD)
    lName.append('avg')
    return lQD,lName

def CalcDiffPerformPearson(QD,hQEva):
    #using map here
    
    
    #discard those not in QD.hQD
    hInEva = {}
    for qid in QD.hQD.keys():
        hInEva[qid] = hQEva[qid]
    
    lQD = QD.hQD.items()
    lQD.sort(key = lambda item:item[0])
    lEva = hInEva.items()
    lEva.sort(key = lambda item:item[0])
    
    print "[%d] q dt, [%d] eva" %(len(lQD),len(lEva))
    
    x = [item[1] for item in lQD]
    y = [item[1].map for item in lEva]
    
    return pearson(x,y)


import sys

if 4 != len(sys.argv):
    print "3 para: qd dir + baseline eva + output"
    sys.exit()
    
lPerQEva = ReadPerQEva(sys.argv[2])
hQEva = dict(lPerQEva)
lQD,lName = LoadAllQueryDifficulty(sys.argv[1])    

out = open(sys.argv[3],'w')
for i in range(len(lQD)):
    pear = CalcDiffPerformPearson(lQD[i],hQEva)
    print >>out, lName[i] + '\t%f' %(pear)
    
out.close()
    
    
    
    
    
    
    
    
        
