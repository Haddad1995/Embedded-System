from sense_hat import SenseHat
from time import time

def factor(n):
  i=2
  while i<=(n/2):
    if n%i==0:
      print(i)
    i=i+1
start = time()
k=int(input("enter number"))
factor(k)
end = time()
print("Elapsed time: {} seconds".format(end - start))
