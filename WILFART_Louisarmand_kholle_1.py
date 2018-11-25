#!/usr/bin/python3
#WILFART_Louisarmand_kholle_1.py
#MoulesFrites
#25/11/2018
#Script pour la kholle 1, gere une liste .csv

import signal
import sys
import csv
from statistics import mean


def exitproperly(sig, frame):
    sys.stdout.write('\nGood bye misteuuuuuur\n')
    sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)


fileName = 'liste.csv'

def show():

    with open('liste.csv') as csv_file:
        read_csv = csv.reader(csv_file)
        for row in read_csv:
            print(', '.join(row))
    csv_file.close()

def add():
    if len(sys.argv) < 3:
        print("Faudrais ptete mettre des chiffres nan ?")
    else:
        files = open(fileName, "a")
        lenArgs = len(sys.argv) - 2
        for i in range(lenArgs):
            a = i + 2
            if i == 0:
                tabInsert = '\n' + sys.argv[a] + ','
            elif i == lenArgs - 1:
                tabInsert = sys.argv[a]
            else:
                tabInsert = sys.argv[a] + ','
            files.write(tabInsert)
        files.close()

def rm():
    remove = open(fileName, "w")
    remove.write('')
    remove.close()

def minmaxmoysum():
    if len(sys.argv) < 3:
        print("Faudrais ptete mettre des arguments nan ?")
    else:
        varTab = []
        a = 0
        with open('liste.csv') as csv_file:
            read_csv = csv.reader(csv_file)
            for row in read_csv:
                a += 1
                varTab.append(row)
            csv_file.close()
        if str(sys.argv[2]) == "--min":
            print(min(varTab))
        elif str(sys.argv[2]) == "--max":
            print(max(varTab))
        elif str(sys.argv[2]) == "--moy":
            print(mean(varTab))
        elif str(sys.argv[2]) == "--sum":
            print(a)

def choice():
    if len(sys.argv) < 2:
        print("Faudrais ptete mettre des arguments nan ?")
    else:
        if str(sys.argv[1]) == "-l":
            show()
        elif str(sys.argv[1]) == "-a":
            add()
        elif str(sys.argv[1]) == "-c":
            rm()
        elif str(sys.argv[1]) == "-s":
            minmaxmoysum()
    
choice()
