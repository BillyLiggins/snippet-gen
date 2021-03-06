## !/usr/bin/env python
## -*- coding: utf-8 -*-
import numpy as np
import pprint as pp

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
    return classnames

def getConstrutor(files,classnames):
    """Returns a list of constructors in file"""
    construtors=[]
    for name in classnames:
        strlist=[name+"(",";"]
        for file in files:
            with open(file) as f:
                basename= file.split(".")[0]
                # print "basename = ", basename
                for x in f:
                    if all( xx in x for xx in strlist):
                        if "virtual" not in x:
                            print "Inside the Loop",x
                            name= x.split(";")
                            print name
                            construtors.append(x.split(";")[0].lstrip(" "))
                            print "bottom ", x.split(";")[0].lstrip(" ")
                            print construtors
                            print "++++++++++++"
    return construtors

def makeSnippet(construtors):
    """Returns a list of constructors in file"""
    snippets=[]
    for construtor in construtors:
        print "From inside the snippet maker"
        basename= construtor.split("(")[0]
        varibles= (construtor.split("(")[1]).split(")")[0]
        # varibles=np.array(varibles.split(","))
        varibles=varibles.split(",")
        print basename
        print varibles
        list1=["${"+str(varibles.index(i)+2)+":"+i.split(" ")[-1]+"}" for i in varibles]
        print basename+"* "+"${1:name} = new "+basename+"("+",".join(list1)+");"
        snippets.append(basename+"* "+"${0:name} = new "+basename+"("+",".join(list1)+");")
        # print [i.split(" ")[-1] for i in varibles]
        # print [varibles.index(i) for i in varibles]
        # print ["{"+str(varibles.index(i))+":"+i.split(" ")[-1]+"}" for i in varibles]
    pp.pprint(snippets)
    return snippets


def formatSnippet(snips):
    """"""
    snippets=[]
    first=""
    counter=0
    for snip in snips:
        basename=snip.split("*")[0]
        if first==basename:
            counter=counter+1
        else:
            counter=0
        snippets.append("snippet "+basename+str(counter)+"\n\t"+snip+"\n")
        first=basename         
        
    pp.pprint(snippets)
    return snippets

def printToFile(file,snips):
    f=open(file,"w+")
    for snip in snips:
        f.write(snip)
    f.close()


def main():
    """main function."""
    f=findHead("*.h")
    findCon(f)
    classnames=findClassCon(f)
    print classnames
    print "------------------------------------------------------------"
    constlist=getConstrutor(f,classnames)
    print constlist
    print "------------------------------------------------------------"
    snips=makeSnippet(constlist)
    forprint=formatSnippet(snips)
    printToFile("output.txt",forprint)
    
if __name__ == '__main__':
    main()
