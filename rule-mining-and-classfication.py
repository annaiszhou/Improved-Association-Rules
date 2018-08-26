# -*- coding: utf-8 -*-
#__author__ = 'zww'

from __future__ import division
import copy
import numpy as np
import csv

def loadTrainSet(source):
    csv_reader = csv.reader(open(source,'r'))
    writer = []
    for row in csv_reader:
        writer.append(row)
    return writer

def createDataStructure(pre):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    structure = {'benign':{'member':[],'attribute':{}},
                 'malignant':{'member':[],'attribute':{}}}
    member = []
    attribute = {}
    num = 0
    middle = {}
    for pres in pre:
        num+=1
        member = structure.get(pres[9]).get('member')
        member.append(num)
        if middle.has_key(pres[0]) == False:
            middle[pres[0]] = {'member':[num]}
        else:
            middle.get(pres[0]).get('member').append(num)
        if middle.has_key(pres[1]) == False:
            middle[pres[1]] = {'member':[num]}
        else:
            middle.get(pres[1]).get('member').append(num)            
        if middle.has_key(pres[2]) == False:
            middle[pres[2]] = {'member':[num]}
        else:
            middle.get(pres[2]).get('member').append(num)
        if middle.has_key(pres[3]) == False:
            middle[pres[3]] = {'member':[num]}
        else:
            middle.get(pres[3]).get('member').append(num)   
        if middle.has_key(pres[4]) == False:
            middle[pres[4]] = {'member':[num]}
        else:
            middle.get(pres[4]).get('member').append(num)
        if middle.has_key(pres[5]) == False:
            middle[pres[5]] = {'member':[num]}
        else:
            middle.get(pres[5]).get('member').append(num)
        if middle.has_key(pres[6]) == False:
            middle[pres[6]] = {'member':[num]}
        else:
            middle.get(pres[6]).get('member').append(num)
        if middle.has_key(pres[7]) == False:
            middle[pres[7]] = {'member':[num]}
        else:
            middle.get(pres[7]).get('member').append(num)
        if middle.has_key(pres[8]) == False:
            middle[pres[8]] = {'member':[num]}
        else:
            middle.get(pres[8]).get('member').append(num)
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                fixmiddle = {}
                fixmiddle = copy.deepcopy(middle)
                v[ks] = fixmiddle
    return structure

def get_median(datamedian):
    datamedian.sort()
    half = len(datamedian)//2
    return (datamedian[half]+datamedian[~half])/2

def get_precents(dataprecent):
    a = np.array((dataprecent))
    b = np.percentile(a,threholdsupport)#threhold
    return b

def get_precentc(dataprecent):
    a = np.array((dataprecent))
    b = np.percentile(a,threholdconfidence)#threhold
    return b
            
def countSupport(structure):
    supportlist = []
    mediansupport = 0
    precentsupport = 0
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    supportlist.append(len(value.get('member')))
    '''
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    if supportset.has_key(key) == False:
                        supportset[key] = value.get('member')
                    else:
                        supportset.get(key).extend(value.get('member'))
    for k,v in supportset.items():
        supportlist.append(len(v))
    '''
    mediansupport = get_median(supportlist)
    precentsupport = get_precents(supportlist)
    return mediansupport,precentsupport

def countConfidence(structure):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    confidencelist = []
    medianconfidence = 0
    percentconfidence = 0
    confidence = 0
    collectA = []
    collectB = []
    collectC = []
    lengthA = 0
    lengthB = 0
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    collectA = value.get('member')
                    collectB = v.get('member')
                    collectC = list(set(collectA)&set(collectB))
                    lengthA = len(collectA)
                    lengthB = len(collectC)
                    if lengthA !=0:
                        confidence = lengthB/lengthA
                    confidencelist.append(confidence)
    medianconfidence = get_median(confidencelist)
    precentconfidence = get_precentc(confidencelist)
    return medianconfidence,precentconfidence   
                    
def createDataStructureSupport(structure,dynamic,adapt):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    num = 0
    delete = 0
    fixstructure = copy.deepcopy(structure)
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    if len(value.get('member'))<dynamic:
                        vs.pop(key)
                        delete+=1
                    num+=1
    if delete!=0:
        if num/delete>2:#meet the demand of half of the whole number, not'>='
            print 'dynamic'
            print '+++++++++++++++++++++++++++++++++++++++++++'
            return structure
        else:
            num = 0
            delete = 0
            for k,v in fixstructure.items():
                for ks,vs in v.items():
                    if ks == 'attribute':
                        for key,value in vs.items():
                            if len(value.get('member'))<adapt:
                                vs.pop(key)
                                delete+=1
                            num+=1
            '''
            for k,v in fixstructure.items():
                for ks,vs in v.items():
                    if ks == 'attribute':            
                        print vs.keys()
            print num,delete
            '''
            print 'adapt'
            print '+++++++++++++++++++++++++++++++++++++++++++'
            return fixstructure
    else:
        print 'dynamic'
        print '+++++++++++++++++++++++++++++++++++++++++++'
        return structure

def createDataStructureSupportConfidence(structure,dynamic,adapt):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    num = 0
    delete = 0
    confidence = 0
    collectA = []
    collectB = []
    collectC = []
    lengthA = 0
    lengthB = 0
    fixstructure = copy.deepcopy(structure)
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    collectA = value.get('member')
                    collectB = v.get('member')
                    collectC = list(set(collectA)&set(collectB))
                    lengthA = len(collectA)
                    lengthB = len(collectC)
                    if lengthA !=0:
                        confidence = lengthB/lengthA
                    if confidence<dynamic:
                        vs.pop(key)
                        #print k,key,confidence,vs.keys()
                        delete+=1
                    num+=1
    if delete!=0:
        if num/delete>2:#meet the demand of half of the whole number, not'>='
            print 'dynamic'
            print '+++++++++++++++++++++++++++++++++++++++++++'
            return structure
        else:
            num = 0
            delete = 0
            for k,v in fixstructure.items():
                for ks,vs in v.items():
                    if ks == 'attribute':
                        for key,value in vs.items():
                            collectA = value.get('member')
                            collectB = v.get('member')
                            collectC = list(set(collectA)&set(collectB))
                            lengthA = len(collectA)
                            lengthB = len(collectC)
                            if lengthA !=0:
                                confidence = lengthB/lengthA
                            if confidence<adapt:
                                vs.pop(key)
                                #print k,key,confidence,vs.keys()
                                delete+=1
                            num+=1
                        #print k,vs.keys()
            #print num,delete
            print 'adapt'
            print '+++++++++++++++++++++++++++++++++++++++++++'
            return fixstructure
    else:
        print 'dynamic'
        print '+++++++++++++++++++++++++++++++++++++++++++'
        return structure        
    
def createJudge(structure):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    lengthlist = []
    length = 0
    for k,v in structure.items():
        length = 0
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    length+=1
                lengthlist.append(length)
    minlength = min(lengthlist)
    maxlength = max(lengthlist)
    print minlength,maxlength
    return minlength,maxlength

def mergeDataStructure(mergestructure):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    memory = []
    mark1 = ''
    mark2 = ''
    string = ''
    num = 0
    list1 = []
    list2 = []
    list3 = []
    n1 = 0
    n2 = 0
    #add the same thing compare
    #deepcopy first
    for k,v in mergestructure.items():
        memory = []
        for ks,vs in v.items():
            if ks == 'attribute':
                #print k,vs.keys()
                for key,value in vs.items():
                    for keys,values in vs.items():
                        if key!=keys:
                            string = key+','+keys
                            mark1 = string.split(',')
                            num = 0
                            for every in memory:
                                mark2 = every.split(',')
                                if set(mark1)&set(mark2) == set(mark2) or set(mark1)&set(mark2) == set(mark1) or len(list(set(key.split(','))&set(keys.split(','))))!=0:
                                    #print len(set(key.split(','))&set(keys.split(','))),key.split(',')+keys.split(',')
                                    #print key,keys
                                    num+=1
                                    break
                            if num==0:
                                memory.append(string)
                                list1 = value.get('member')
                                list2 = values.get('member')
                                list3 = list(set(list1)&set(list2))
                                vs.update({string:{'member':list3}})
                                #print string
    return mergestructure                       

def createRuleStructure(structure):
    '''
    {'benign': {'member': [1, 2], 
                            'attribute': {'8-low': {'member': [1, 2]}, '1-high': {'member': [2]}, '4-low': {'member': [1, 2]}, 
                                          '7-low': {'member': [1, 2]}, '9-low': {'member': [1, 2]}, '3-low': {'member': [1, 2]}, 
                                          '5-low': {'member': [2]}, '5-high': {'member': [1]}, '1-low': {'member': [1]}, 
                                          '6-low': {'member': [1, 2]}, '2-low': {'member': [1, 2]}}}, 
     'malignant': {'member': [3], 
                               'attribute': {'1-high': {'member': [3]}, '4-high': {'member': [3]}, '3-high': {'member': [3]}, 
                                             '7-high': {'member': [3]}, '2-high': {'member': [3]}, '6-high': {'member': [3]}, 
                                             '5-high': {'member': [3]}, '8-high': {'member': [3]}, '9-high': {'member': [3]}}}}
    '''
    '''previous
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    vs[key].update({'number':len(value.get('member'))})
                    vs[key].pop('member')
        structure[k].update({'number':len(v.get('member'))})
        structure[k].pop('member')
    return structure
    '''
    num = 0
    delete = 0
    confidence = 0
    collectA = []
    collectB = []
    collectC = []
    lengthA = 0
    lengthB = 0
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    if len(key.split(','))!=len(set(key.split(','))):
                        #print len(set(key.split(','))),len(key.split(','))
                        vs.pop(key)
    for k,v in structure.items():
        for ks,vs in v.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    collectA = value.get('member')
                    collectB = v.get('member')
                    collectC = list(set(collectA)&set(collectB))
                    lengthA = len(collectA)
                    lengthB = len(collectC)
                    if lengthA!=0:
                        confidence = lengthB/lengthA
                    vs[key].update({'number':len(value.get('member'))})
                    vs[key].update({'confidence':confidence})
                    vs[key].pop('member')                    
        structure[k].update({'number':len(v.get('member'))})
        structure[k].pop('member')
    return structure

def createRule(dataset):
    DataStructure = createDataStructure(dataset)
    DynamicSupportlist = [0]
    AdaptiveSupportlist = [0]
    i = 0
    print DataStructure
    #print '+++++++++++++++++++++++++++++++++++++++++++'
    Judge,Judge1 = createJudge(DataStructure)
    print 'Judge:',Judge
    print '+++++++++++++++++++++++++++++++++++++++++++'
    while Judge1>threholdjudge:#threhold
        DynamicSupport,AdaptiveSupport = countSupport(DataStructure)
        print 'DynamicSupport:',DynamicSupport
        print 'AdaptiveSupport',AdaptiveSupport
        print '+++++++++++++++++++++++++++++++++++++++++++'
        DataStructureSupport = createDataStructureSupport(DataStructure,DynamicSupport,AdaptiveSupport)
        #print DataStructureSupport
        #print '+++++++++++++++++++++++++++++++++++++++++++'
        DynamicConfidence,AdaptiveConfidence = countConfidence(DataStructureSupport)
        print 'DynamicConfidence:',DynamicConfidence
        print 'AdaptiveConfidence',AdaptiveConfidence
        print '+++++++++++++++++++++++++++++++++++++++++++'
        DataStructureSupportConfidence = createDataStructureSupportConfidence(DataStructureSupport,DynamicConfidence,AdaptiveConfidence)
        #print DataStructureSupportConfidence
        #print '+++++++++++++++++++++++++++++++++++++++++++'
        DataStructure = mergeDataStructure(DataStructureSupportConfidence)
        #print DataStructure
        #print '+++++++++++++++++++++++++++++++++++++++++++'
        Judge,Judge1 = createJudge(DataStructure)
        print 'minJudge:',Judge
        print 'maxJudge:',Judge1
        print '+++++++++++++++++++++++++++++++++++++++++++'
        if DynamicSupport == DynamicSupportlist[i] and AdaptiveSupport == AdaptiveSupportlist[i]:
            #print DataStructure
            #print '+++++++++++++++++++++++++++++++++++++++++++'
            RuleStructure = createRuleStructure(DataStructure)
            return RuleStructure
        else:
            DynamicSupportlist.append(DynamicSupport)
            AdaptiveSupportlist.append(AdaptiveSupport)
            i+=1
    #print DataStructure
    #print '+++++++++++++++++++++++++++++++++++++++++++'
    RuleStructure = createRuleStructure(DataStructure)
    return RuleStructure

def createSortRule(Rule):
    temp = []
    tempconfidence = [float('inf')]
    tempsupport = [float('inf')]
    templength = [float('inf')]
    i = 0
    j = 0
    k = 0
    i=0
    ans = {}
    for kss,vss in Rule.items():
        temp = []
        for ks,vs in vss.items():
            if ks == 'attribute':
                for key,value in vs.items():
                    i=0
                    j=0
                    k=0
                    for everyc in tempconfidence:
                        if value.get('confidence')>float(everyc):
                            i+=1
                        elif value.get('confidence')==float(everyc):
                            j=0
                            for everys in tempsupport[i:]:
                                if value.get('number')>float(everys):
                                    j+=1                                   
                                elif value.get('number')==float(everys):
                                    k=0
                                    for everyl in templength[i+j:]:
                                        if len(key.split(','))>float(everyl):
                                            k+=1
                                        else:
                                            tempconfidence.insert(i+j+k,value.get('confidence'))
                                            tempsupport.insert(i+j+k,value.get('number'))
                                            templength.insert(i+j+k,len(key.split(',')))
                                            temp.insert(i+j+k,key.split(','))
                                            break
                                    break
                                else:
                                    tempconfidence.insert(i+j,value.get('confidence'))
                                    tempsupport.insert(i+j,value.get('number'))
                                    templength.insert(i+j,len(key.split(',')))
                                    temp.insert(i+j,key.split(','))
                                    break
                            break
                        else:
                            tempconfidence.insert(i,value.get('confidence'))
                            tempsupport.insert(i,value.get('number'))
                            templength.insert(i,len(key.split(',')))
                            temp.insert(i,key.split(','))
                            break
        ans[kss]=temp
    return ans


def loadRule(SortRule):
    fixRule =  SortRule
    return fixRule

def loadTestData(source):
    csv_reader = csv.reader(open(source,'r'))
    writer = []
    for row in csv_reader:
        writer.append(row)
    return writer

def createClassification(rule,data):
    for datas in data:
        for k,v in rule.items():
            if len(datas) == 10:#catch automatically
                for vs in v:
                    if set(vs)&set(datas)==set(vs):
                        datas.append(k)
                        break
            else:
                break
    #for row in data:
        #print row[-1],row[-2]
    return data

def judgeAccuracy1(classdata):
    judgeline = 0
    allline = 0
    yes = [0,0]
    no = [0,0]
    for row in classdata:
        if len(row) == 11:
            judgeline+=1
            if row[-2] == 'benign':
                if row[-1] == row[-2]:
                    yes[0]+=1
                else:
                    yes[1]+=1
            else:
                if row[-1] == row[-2]:
                    no[1]+=1
                else:
                    #print row[-1],row[-2]
                    no[0]+=1
        allline+=1
    result = judgeline/allline
    return result,yes,no

def judgeAccuracy2(classdata):
    middlefile = 'breast_test_label_middle.csv'
    csv_writer = csv.writer(open(middlefile,'wb+'))
    writer = []
    judgeline = 0
    allline = 0
    yes = [0,0]
    no = [0,0]
    for row in classdata:
        if len(row) == 11:
            judgeline+=1
            if row[-2] == 'benign':
                if row[-1] == row[-2]:
                    yes[0]+=1
                else:
                    yes[1]+=1
            else:
                if row[-1] == row[-2]:
                    no[1]+=1
                else:
                    #print row[-1],row[-2]
                    no[0]+=1
        else:
            csv_writer.writerow(row)
        allline+=1
    result = judgeline/allline
    return result,yes,no

def judgeAccuracy3(classdata):
    middlefile = 'breast_train_label_middle.csv'
    csv_writer = csv.writer(open(middlefile,'wb+'))
    writer = []
    judgeline = 0
    allline = 0
    yes = [0,0]
    no = [0,0]
    for row in classdata:
        if len(row) == 11:
            judgeline+=1
            if row[-2] == 'benign':
                if row[-1] == row[-2]:
                    yes[0]+=1
                else:
                    yes[1]+=1
            else:
                if row[-1] == row[-2]:
                    no[1]+=1
                else:
                    #print row[-1],row[-2]
                    no[0]+=1
        else:
            csv_writer.writerow(row)
        allline+=1
    result = judgeline/allline
    return result,yes,no

if __name__ == '__main__':
    #threhold
    threholdsupport=75
    threholdconfidence=60
    threholdjudge=10#155
    print '------------first classfication------------'
    trainfile = 'breast_train_label.csv'#breast_train_label.csv
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '-----------------loadDataSet---------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    TrainSet = loadTrainSet(trainfile)
    print 'finish'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '-----------------createRule----------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    Rule = createRule(TrainSet)
    print 'Rule:'
    print Rule
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '----------------createPredict--------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    SortRule = createSortRule(Rule)
    print SortRule
    testfile = 'breast_test_label.csv'
    Rule = loadRule(SortRule)
    #print Rule
    TestData = loadTestData(testfile)
    Classification = createClassification(Rule,TestData)
    Frequency1,Accuracyyes1,Accuracyno1 = judgeAccuracy2(Classification)
    print 'Frequency1:',Frequency1
    print 'Accuracyyes1:',Accuracyyes1
    print 'Accuracyno1:',Accuracyno1
    testfile = 'breast_train_label.csv'
    Rule = loadRule(SortRule)
    #print Rule
    TestData = loadTestData(testfile)
    Classification = createClassification(Rule,TestData)
    Frequencynot,Accuracynot,Accuracynot = judgeAccuracy3(Classification)
    print '------------second classfication------------'
    trainfile = 'breast_train_label_middle.csv'#breast_train_label.csv    
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '-----------------loadDataSet---------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    TrainSet = loadTrainSet(trainfile)
    print 'finish'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '-----------------createRule----------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    Rule = createRule(TrainSet)
    print 'Rule:'
    print Rule
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print '----------------createPredict--------------'
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    SortRule = createSortRule(Rule)
    print SortRule
    testfile = 'breast_test_label_middle.csv'
    Rule = loadRule(SortRule)
    #print Rule
    TestData = loadTestData(testfile)
    Classification = createClassification(Rule,TestData)
    Frequency2,Accuracyyes2,Accuracyno2 = judgeAccuracy1(Classification)
    print 'Frequency2:',Frequency2
    print 'Accuracyyes2:',Accuracyyes2
    print 'Accuracyno2:',Accuracyno2
    print '----------------at last--------------------'
    print 'Accuracyyes:',[Accuracyyes2[i]+Accuracyyes1[i] for i in range(min(len(Accuracyyes2),len(Accuracyyes1)))]
    print 'Accuracyno:',[Accuracyno2[i]+Accuracyno1[i] for i in range(min(len(Accuracyno2),len(Accuracyno1)))]
    m = (sum(Accuracyyes1)+sum(Accuracyno1))/Frequency1
    n = sum(Accuracyyes1)+sum(Accuracyno1)+sum(Accuracyyes2)+sum(Accuracyno2)
    print m,n
    print 'Call:',n/m
    p = (Accuracyyes1[0]+Accuracyno1[1]+Accuracyyes2[0]+Accuracyno2[1])/n
    #print Accuracyyes1[0]+Accuracyno1[1]+Accuracyyes2[0]+Accuracyno2[1],n
    print 'Accuracy',p
