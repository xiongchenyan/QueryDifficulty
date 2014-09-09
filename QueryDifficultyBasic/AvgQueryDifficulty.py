'''
Created on Sep 9, 2014
get avg of given 30 splits
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


import sys

if 3 != len(sys.argv):
    print 'all q difficulty dir + out dir'
    sys.exit()
    
if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])
    
lQD = LoadAllQueryDifficulty(sys.argv[1])[0]

AvgQD = lQD[len(lQD) - 1]

lQDScore = AvgQD.hQD.items()

Mid = len(lQDScore) / 2

out = open(sys.argv[2] + '/res1','w')
for qid,score in lQDScore[:Mid]:
    print >>out, '%d %f' %(qid,score)
    
out.close()
out  = open(sys.argv[2] + 'res2','w')
for qid,score in lQDScore[Mid:]:
    print >> out, '%d %f' %(qid,score)
out.close()


