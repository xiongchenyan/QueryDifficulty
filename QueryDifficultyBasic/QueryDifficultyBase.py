'''
Created on Sep 9, 2014
load one prediction score from data
@author: cx
'''


class QueryDifficultyBaseC(object):
    def __init__(self,Dir = ''):
        self.Init(Dir)
        if Dir != '':
            self.load(Dir)
            
            
    def Init(self,Dir):
        self.Dir = Dir
        self.hQD = {}
        
        
    def load(self,Dir):
        lFName = ['res1','res2']
        for fname in lFName:
            for line in open(Dir + '/' + fname):
                vCol = line.strip().split()
                qid = int(vCol[0])
                score = float(vCol[1])
                self.hQD[qid] = score
        return True
    
    @classmethod
    def Avg(cls,lQueryDiffC):
        res = QueryDifficultyBaseC()
        
        hQCnt = {}
        hQSum = {}
        
        for QD in lQueryDiffC:
            for qid,score in QD.hQD.items():
                if not qid in hQSum:
                    hQSum[qid] = score
                    hQCnt[qid] = 1
                    continue
                hQSum[qid] += score
                hQCnt[qid] += 1
        for qid in hQSum.keys():
            hQSum[qid] /= float(hQCnt[qid])
            
        res.hQD = hQSum
        return res
            
            
    
    
    
            
            
