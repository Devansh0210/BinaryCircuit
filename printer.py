#!/usr/bin/env python
# coding: utf-8

from parserBool import BoolEquation
from graycode import *
import numpy as np
import math

class TruthTable(BoolEquation):

      def __init__(self,eqn):
            super().__init__(eqn)
      
      def printTable(self):
            headline = "Truth Table :\n\n|"
            no = len(self.literals)
            for lit in self.literals:
                  headline = headline + f' {lit} |'
            
            headline = headline + ' Output|\n'
            headline = headline + ''.join(['-']*(len(headline)-16))+'\n'
            func = self.exc
            binNo = binaryGen(no)
            for n in binNo:
                  temp = list(n)
                  temp = [int(j) for j in temp]
                  out = func(*temp)
                  line = '|'
                  for c in temp:
                        line = line + f' {c} |'
                  line = line + f'   {out}   |\n'
                  headline = headline + line       

            return (headline)

class KMap(BoolEquation):
      
      def __init__(self, eqn):
            super().__init__(eqn)
            self.grayMatrix()

      def grayMatrix(self):
            func = self.exc
            no = len(self.literals)
            self.resultMat = np.zeros((1,2**no),dtype=int)
            binNo = binaryGen(no)
            i = 0       
            for num in binNo:
                  temp = conv_grayCode(num)
                  # self.li.append(temp)
                  temp = list(temp)
                  temp = [int(j) for j in temp]
                  self.resultMat[0,i] = func(*temp)
                  i = i + 1
            
            self.Y = math.floor(no/2)
            self.X = math.ceil(no/2)
            self.dimY = 2**self.Y
            self.dimX = 2**self.X
            self.resultMat = np.reshape(self.resultMat,(self.dimY,self.dimX))
            for h in range(1,self.dimY,2):
                  self.resultMat[h,:] = self.resultMat[h,::-1]                  
            self.resultMat = self.resultMat.astype(str)
            return (self.resultMat)
      
      def printKMap(self):
            table = 'KMap : \n\n___|'
            grayX = [conv_grayCode(s) for s in binaryGen(self.X)]
            grayY = [conv_grayCode(d) for d in binaryGen(self.Y)]
            for x in grayX:
                  table = table + ''.join([' ']*(3-len(x))) + f'{x} |' 
            line = ""
            for l in range(self.dimY):
                  line = line + ''.join([' ']*(3-len(grayY[0]))) + f'{grayY[l]}|  '
                  line = line + ' |  '.join(list(self.resultMat[l,:]))
                  line = line + ' |\n'

            table = table + '\n' + line
            return table

class Minterms:

      def __init__(self,no,minterms):
            self.minterms = np.array(minterms)
            # print(self.minterms)
            self.no = no
            self.literals = [chr(c) for c in range(65,65+no)]
            # self.generateTable()
            # self.generateKmap()
            # self.printKMap()


            
      def generateTable(self):
            self.output = np.zeros(2**(self.no),dtype=int)
            self.output[self.minterms] = 1
            headline = "Truth Table :\n\n|"
            
            for lit in self.literals:
                  headline = headline + f' {lit} |'
            
            headline = headline + ' Output|\n'
            headline = headline + ''.join(['-']*(len(headline)-16))+'\n'
            
            i = 0
            binNo = binaryGen(self.no)
            for n in binNo:
                  temp = list(n)
                  temp = [int(j) for j in temp]
                  out = self.output[i]
                  line = '|'
                  for c in temp:
                        line = line + f' {c} |'
                  line = line + f'   {out}   |\n'
                  headline = headline + line       
                  i = i + 1

            return (headline)
      
      def generateKmap(self):
            # func = self.exc
            # no = len(self.literals)
            self.resultMat = np.zeros((1,2**self.no),dtype=int)
            binNo = binaryGen(self.no)
            grayNo = [binTodec(conv_grayCode(decTobin(k))) for k in range(2**self.no)]
            print(grayNo)
            for k in self.minterms:
                  self.resultMat[0,np.where(grayNo==k)[0][0]] = 1
            
            # func = self.exc
            # no = len(self.literals)
            # self.resultMat = np.zeros((1,2**no),dtype=int)
            # binNo = binaryGen(no)
            # i = 0       
            # self.li = []     
            # for num in binNo:
            #       temp = conv_grayCode(num)
            #       self.li.append(temp)
            #       temp = list(temp)
            #       temp = [int(j) for j in temp]
            #       self.resultMat[0,i] = func(*temp)
            #       i = i + 1
            
            self.Y = math.floor(self.no/2)
            self.X = math.ceil(self.no/2)
            self.dimY = 2**self.Y
            self.dimX = 2**self.X
            self.resultMat = np.reshape(self.resultMat,(self.dimY,self.dimX))
            for h in range(1,self.dimY,2):
                  self.resultMat[h,:] = self.resultMat[h,::-1]                  
            self.resultMat = self.resultMat.astype(str)
            return (self.resultMat)
            self.Y = math.floor(no/2)
            self.X = math.ceil(no/2)
            self.dimY = 2**self.Y
            self.dimX = 2**self.X
            self.resultMat = np.reshape(self.resultMat,(self.dimY,self.dimX))
            for h in range(1,self.dimY,2):
                  self.resultMat[h,:] = self.resultMat[h,::-1]                  
            self.resultMat = self.resultMat.astype(str)
            return (self.resultMat)

      def printKMap(self):
            self.generateKmap()
            table = 'KMap : \n\n___|'
            grayX = [conv_grayCode(s) for s in binaryGen(self.X)]
            grayY = [conv_grayCode(d) for d in binaryGen(self.Y)]
            for x in grayX:
                  table = table + ''.join([' ']*(3-len(x))) + f'{x} |' 
            line = ""
            for l in range(self.dimY):
                  line = line + ''.join([' ']*(3-len(grayY[0]))) + f'{grayY[l]}|  '
                  line = line + ' |  '.join(list(self.resultMat[l,:]))
                  line = line + ' |\n'

            table = table + '\n' + line
            return (table)

# t1.generateTable()

