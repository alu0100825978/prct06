#!/usr/bin/python
import sys

#funcion aproximacion de pi
def aprox(n):
  suma=0.0
  for i in range (1,n+1):
    x_i= float ((i-0.5)/n)
    fx_i= float (4./(1+x_i**2))
    suma = suma + fx_i
  r = float (1/float(n) * suma)
  return r
  
n = int(sys.argv[1])
m = int(sys.argv[2])
l = []  
for i in range (1,m+1): 
  r=aprox(i*n)
  l=l+[r]

print l
  