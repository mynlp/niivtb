#!/usr/bin/env python3
import os
import shutil
import sys

PJoin = os.path.join

def CreateOutDir(annDir,annFDir):
    shutil.rmtree(annFDir, ignore_errors=True)
    os.mkdir(annFDir)
    subannFDirs = [PJoin(annFDir, dir) for dir in os.listdir(annDir)]
    for subannFDir in subannFDirs:
        os.mkdir(subannFDir)
        temp = subannFDir.split('/')
        subannDir = PJoin(annDir, temp[len( temp)-1])
        if os.path.isdir(subannDir) == True:
            subsubannFDirs = [PJoin(subannFDir, dir) for dir in os.listdir(subannDir)]
            for subsubannFDir in subsubannFDirs:
                os.mkdir(subsubannFDir)

def GetFiles(path):
    file_list, dir_list = [], []
    for dir, subdirs, files in os.walk(path):
        file_list.extend([PJoin(dir, f) for f in files])
        dir_list.extend([PJoin(dir, d) for d in subdirs])
    return file_list, dir_list

def wordCount(str):
    if str == "":
        return 0
    return str.count(' ') - 1

def Compare_Files(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    l1 = f1.readlines()
    l2 = f2.readlines()
    if len(l1) != len(l2):
        print("len khac nhau", file1, file2)
        f1.close()
        f2.close()
        return 0
    i=0
    while i<len(l1):
        n = int(''.join(j for j in l1[i] if j.isdigit()))
        if n != wordCount(l2[i]):
            print(file1, file2)
            print(n, l2[i], wordCount(l2[i]))
            f1.close()
            f2.close()
            return 0
        i+=1
    f1.close()
    f2.close()
    return 1

def GetFilename(path):
    s = path.split('/')
    return s[len(s)-1]

def IsValidFile(file, idDir):
    if file.find('.DS_Store') != -1:
        return 0
    idFiles, idDirs = GetFiles(os.path.expanduser(idDir))
    for f in idFiles:
        if f.find('.DS_Store') == -1:
            f1 = GetFilename(f)
            f2 = GetFilename(file)
            if f1 == f2:
                if Compare_Files(f, file) == 1:
                    return 1
    return 0

def SearchFile(rawfile,annFiles):
    for file in annFiles:
        fn = GetFilename((rawfile))
        temp = fn.split('.')
        if rawfile.find("NIIVTB-1") != -1:
            filename = '_'+temp[0] + '.'
        else:
            filename = temp[0] + '.'
        if file.find(filename) != -1:
            return file
    return -1

def MergeString(str1,str2):
    l1 = str1.split(' ')
    l2 = str2.split('_SYLLABLE_WORD')
    i = 0
    j=1
    s=''
    while(i<len(l2)-1):
        s2 = l2[i]
        n = [int(k) for k in s2.split() if k.isdigit()]
        s2 = s2.rsplit(' ', 1)[0]
        s1=''
        wC = 0
        while(wC<n[len(n)-1]-1) and j<len(l1)-1:
            s1 = s1 + l1[j] +'_'
            wC+=1
            j+=1
        if j < len(l1)-1:
            s1 = s1+l1[j]
        s = s + s2 + ' ' + s1
        j+=1
        i+=1
    s = s + l2[len(l2)-1]
    return s

def MergeFile(rawfile, annFile, outFile):
    f1 = open(rawfile)
    f2 = open(annFile)
    f3 = open(outFile,'w')
    l1 = f1.readlines()
    l2 = f2.readlines()
    i = 0
    while i < len(l1):
        s = MergeString(l1[i],l2[i])
        f3.write(s)
        i+=1
    f1.close()
    f2.close()
    f3.close()

def CreateTree(rawfile, annDir, annFDir):
    annFiles, annDirs = GetFiles(os.path.expanduser(annDir))
    annFile = SearchFile(rawfile,annFiles)
    if annFile != -1:
        temp = annFile.split('/')
        outFile = annFDir + '/' + temp[len(temp)-3] + '/' + temp[len(temp)-2] + '/' + temp[len(temp)-1]
        MergeFile(rawfile, annFile, outFile)
    else:
        print('File not found.', rawfile)


fpath = os.path.dirname(os.getcwd())
annDir = PJoin(fpath, sys.argv[1])
print('Processing ', sys.argv[1], '...')
annFDir = annDir + "-Finished"
CreateOutDir(annDir,annFDir)
invalidFile = open("invalidFiles.txt",'w')
rawDir = annDir + "-RawText"
idDir = annDir + "-ID"
rawFiles, rawDirs = GetFiles(os.path.expanduser(rawDir))

for file in rawFiles:
    if IsValidFile(file,idDir) == 1:
        CreateTree(file, annDir,annFDir)
    else:
        print("Invalid: ", file)
        invalidFile.write(file)
        invalidFile.write('\n')
invalidFile.close()

print('Done.')
        

