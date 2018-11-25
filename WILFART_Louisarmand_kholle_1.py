#!/usr/bin/python3
#WILFART_Louisarmand_kholle_1.py
#MoulesFrites
#25/11/2018
#Script pour la kholle 1, gere une liste .csv

import signal
import sys
import csv


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
        files = open(fileName, "wb")
        writer = csv.writer(files, delimiter=",")
        lenArgs = len(sys.argv) - 2
        for i in range(lenArgs):
            test = []
            a = i + 2
            writer.writerow( (int(sys.argv[a])) )


def choice():
    if len(sys.argv) < 2:
        print("Faudrais ptete mettre des arguments nan ?")
    else:
        if str(sys.argv[1]) == "-l":
            show()
        elif str(sys.argv[1]) == "-a":
            add()
    
choice()
