# -*- coding: utf-8 -*-
# __author__ = 'zww'
# train have two item list in one row
# operate manually

from __future__ import division
from sklearn import cross_validation
import csv
import numpy as np

def get_median(datapercent):
    a = np.array((datapercent))
    b = np.percentile(a,50)
    return b

def get_precentpre(dataprecent):
    a = np.array((dataprecent))
    b = np.percentile(a,25)
    return b

def get_precentpro(dataprecent):
    a = np.array((dataprecent))
    b = np.percentile(a,75)
    return b

if __name__ == '__main__':
    sourcefile = ['breast.csv']
    for source in sourcefile:
        s = open(source,'r')
        csv_reader = csv.reader(s)
        #name = source.split('.')[0]+'_label.csv'
        #csv_writer = csv.writer(open(name,'wb+'))
        writerlist1 = []
        writerlist2 = []
        writerlist3 = []
        writerlist4 = []
        writerlist5 = []
        writerlist6 = []
        writerlist7 = []
        writerlist8 = []
        writerlist9 = []
        writer=[]
        for row in csv_reader:
            if row[1]!='?':
                writerlist1.append(int(row[1]))
            if row[2]!='?':
                writerlist2.append(int(row[2]))
            if row[3]!='?':
                writerlist3.append(int(row[3]))
            if row[4]!='?':
                writerlist4.append(int(row[4]))
            if row[5]!='?':
                writerlist5.append(int(row[5]))
            if row[6]!='?':
                writerlist6.append(int(row[6]))
            if row[7]!='?':
                writerlist7.append(int(row[7]))
            if row[8]!='?':
                writerlist8.append(int(row[8]))
            if row[9]!='?':
                writerlist9.append(int(row[9]))
        writer.append([get_median(writerlist1),get_precentpre(writerlist1),get_precentpro(writerlist1)])
        writer.append([get_median(writerlist2),get_precentpre(writerlist2),get_precentpro(writerlist2)])
        writer.append([get_median(writerlist3),get_precentpre(writerlist3),get_precentpro(writerlist3)])
        writer.append([get_median(writerlist4),get_precentpre(writerlist4),get_precentpro(writerlist4)])
        writer.append([get_median(writerlist5),get_precentpre(writerlist5),get_precentpro(writerlist5)])
        writer.append([get_median(writerlist6),get_precentpre(writerlist6),get_precentpro(writerlist6)])
        writer.append([get_median(writerlist7),get_precentpre(writerlist7),get_precentpro(writerlist7)])
        writer.append([get_median(writerlist8),get_precentpre(writerlist8),get_precentpro(writerlist8)])
        writer.append([get_median(writerlist9),get_precentpre(writerlist9),get_precentpro(writerlist9)])
        print writer
    s.close()
    sourcefile = open('breast.csv','r')
    trainfile = open('breast_train.csv','w')
    #validfile = open('breast_valid.csv','w')
    testfile = open('breast_test.csv','w')
    c = []
    j = 0

    for line in sourcefile:
        c.append(line)
     
    c_train,c_test = cross_validation.train_test_split(c,test_size = 0.25)
    for i in c_test:
        testfile.write(i)
    for i in c_train:
        trainfile.write(i)
    '''
    c_train,c_valid = cross_validation.train_test_split(c_trainvalid,test_size = 0.1)
    for i in c_train:
        trainfile.write(i)
    for i in c_valid:
        validfile.write(i)
    '''
    sourcefile.close()
    trainfile.close()
    testfile.close()
    sourcefile2 = ['breast_test.csv','breast_train.csv']
    for source in sourcefile2:
        csv_reader = csv.reader(open(source,'r'))
        name = source.split('.')[0]+'_label.csv'
        csv_writer = csv.writer(open(name,'wb+'))
        for row in csv_reader:
            writerlist = []
            if row[1]!='?':
                if int(float(row[1]))<=2:
                    writerlist.append('1-low')
                elif 2<int(float(row[1])) and int(float(row[1]))<=4:
                    writerlist.append('1-littlelow')
                elif 4<int(float(row[1])) and int(float(row[1]))<=6:
                    writerlist.append('1-littlehigh')
                else:
                    writerlist.append('1-high')
            else:
                writerlist.append('1-littlehigh')
            if row[2]!='?':
                if int(float(row[2]))<=1:
                    writerlist.append('2-low')
                elif 1<int(float(row[2])) and int(float(row[2]))<=5:
                    writerlist.append('2-middle')
                else:
                    writerlist.append('2-high')
            else:
                writerlist.append('2-middle')
            if row[3]!='?':
                if int(float(row[3]))<=1:
                    writerlist.append('3-low')
                elif 1<int(float(row[3])) and int(float(row[3]))<=5:
                    writerlist.append('3-middle')
                else:
                    writerlist.append('3-high')
            else:
                writerlist.append('3-middle')
            if row[4]!='?':
                if int(float(row[4]))<=1:
                    writerlist.append('4-low')
                elif 1<int(float(row[4])) and int(float(row[4]))<=4:
                    writerlist.append('4-middle')
                else:
                    writerlist.append('4-high')
            else:
                writerlist.append('4-middle')
            if row[5]!='?':
                if int(float(row[5]))<=2:
                    writerlist.append('5-low')
                elif 2<int(float(row[5])) and int(float(row[5]))<=4:
                    writerlist.append('5-middle')
                else:
                    writerlist.append('5-high')
            else:
                writerlist.append('5-middle')
            if row[6]!='?':
                if int(float(row[6]))<=1:
                    writerlist.append('6-low')
                elif 1<int(float(row[6])) and int(float(row[6]))<=6:
                    writerlist.append('6-middle')
                else:
                    writerlist.append('6-high')
            else:
                writerlist.append('6-middle')                
            if row[7]!='?':
                if int(float(row[7]))<=2:
                    writerlist.append('7-low')
                elif 2<int(float(row[7])) and int(float(row[7]))<=3:
                    writerlist.append('7-littlelow')
                elif 3<int(float(row[7])) and int(float(row[7]))<=5:
                    writerlist.append('7-littlehigh')
                else:
                    writerlist.append('7-high')
            else:
                writerlist.append('7-littlehigh')
            if row[8]!='?':
                if int(float(row[8]))<=1:
                    writerlist.append('8-low')
                elif 1<int(float(row[8])) and int(float(row[8]))<=4:
                    writerlist.append('8-middle')
                else:
                    writerlist.append('8-high')
            else:
                writerlist.append('8-middle')
            if row[9]!='?':
                if int(float(row[9]))<=1:
                    writerlist.append('9-low')
                else:
                    writerlist.append('9-high')
            else:
                writerlist.append('9-hign')
            if row[10]!='?':
                if int(float(row[10]))==2:
                    writerlist.append('benign')
                else:
                    writerlist.append('malignant')
            else:
                writerlist.append('benign')#benign is more

            csv_writer.writerow(writerlist)

