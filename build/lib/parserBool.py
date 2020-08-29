#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math
import re

class BoolEquation:

      def __init__(self,eqn):
            self.eqn = eqn
            self.literals = None
            self.convFunc()
            self.exc = self.execFunc()

      def convFunc(self):
            mateqn = re.sub(r"([A-Z])",r"(\1)",self.eqn)
            mateqn = re.sub(r"\(([A-Z])\)'",r"(not \1)",mateqn)
            mateqn = re.sub(r"\+",r") or (",mateqn)
            mateqn = re.sub(r"[\)][\(]" , r") and (",mateqn)
            mateqn = '(' + mateqn + ')'
            
            self.operation = mateqn
            # return mateqn

      def execFunc(self):
            lits = re.findall(r"[A-Z]",self.eqn)
            lits = list(set(lits))
            lits.sort()
            self.literals = lits
            lits = ','.join(lits)
            exc = 'def boolCir(' + lits +'):'+'return '+f'int({self.operation})'
            d = {}
            exec(exc,d)
            return d['boolCir']
      
# eq1 = BoolEquation("ABC")
# func = eq1.exc
