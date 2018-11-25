#!/usr/bin/python3
#WILFART_Louisarmand_kholle_1.py
#MoulesFrites
#25/11/2018
#Script pour la kholle 1, gere une liste .csv

import signal
import sys


def exitproperly(sig, frame):
    sys.stdout.write('\nGood bye misteuuuuuur\n')
    sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)


