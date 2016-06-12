## !/usr/bin/env python
## -*- coding: utf-8 -*-
import numpy as np

import glob

def findHead(path):
    # """Returns a list of header files"""
    return np.array(glob.glob(str(path)))

def findCon(files):
    """Returns a list of constructors in file"""
    for file in files:
        with open(file) as f:
            basename= file.split(".")[0]
            print "basename = ", basename
            for x in f:
                if basename+"(" in x:
                    print x
        
def findClassCon(files):
    """Returns a list of constructors in file"""
    strlist=["class",":","{"]
    classnames=[]
    for file in files:
        with open(file) as f:
            basename= file.split(".")[0]
            print "From inside the class finder"
            print "basename = ", basename
            for x in f:
                if all( xx in x for xx in strlist):
                    print x
                    name= x.split()[1]
                    print name
                    classnames.append(name)
    print classnames
    return classnames

def getConstrutor(files,classnames):
    """Returns a list of constructors in file"""
    for name in classnames:
        strlist=[name+"(",";"]
        construtors=[]
        for file in files:
            with open(file) as f:
                basename= file.split(".")[0]
                print "From inside the con finder"
                print "basename = ", basename
                for x in f:
                    if all( xx in x for xx in strlist):
                        print x
                        # name= x.split()[1]
                        # print name
                        construtors.append(x.rstrip("\n"))
    return construtors

def main():
    """main function."""
    f=findHead("*.h")
    findCon(f)
    classnames=findClassCon(f)
    print classnames
    constlist=getConstrutor(f,classnames)
    print constlist
    
if __name__ == '__main__':
    main()
