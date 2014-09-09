'''
Created on Sep 9, 2014
input: q difficulty + eva result of a method
do: order q by difficulty, and get the avg performance up to this diffculty
    order by increasing difficulty, and decreasing difficulty
output: a increase file, a decreasing file
@author: cx
'''


import site
site.addsitedir('/bos/usr0/cx/PyCode/Geektools')
site.addsitedir('/bos/usr0/cx/PyCode/cxPyLib')
site.addsitedir('/bos/usr0/cx/PyCode/QueryDifficulty')
from QueryDifficultyBasic.QueryDifficultyBase import *
from AdhocEva.AdhocMeasure import *

import sys


def CalcCumulatedPerform(lQOrder,hPerQEva):
    lCumulatedP = []
    lOrderedP = []
    
    for qid in lQOrder:
        if qid in hPerQEva:
            lOrderedP.append(hPerQEva[qid])
    
    for i in range(len(lOrderedP)):
        lCumulatedP.append(lOrderedP[:i + 1])
    return lCumulatedP


if 4 != len(sys.argv):
    print "3 para: q difficulty dir + eva + output pre"
    sys.exit()
    
QD = QueryDifficultyBaseC(sys.argv[1])
lPerQEva = ReadPerQEva(sys.argv[2])
hPerQEva = dict(lPerQEva)



lQD = QD.hQD.items()
lQD.sort(key = lambda item:item[1])
lInc = [item[0] for item in lQD]

lQD.sort(key = lambda item:item[1],reverse = False)
lDes = [item[0] for item in lQD]


lIncCP = CalcCumulatedPerform(lInc,hPerQEva)
lDesCP = CalcCumulatedPerform(lDes,hPerQEva)

OutInc = open(sys.argv[3] + '_inc','w')
OutDes = open(sys.argv[3] + '_des','w')

for measure in lIncCP:
    print >>OutInc,measure.dumps()
    
for measure in lDesCP:
    print >> OutDes, measure.dumps()
    
OutInc.close()
OutDes.close()
    