# -*- coding: utf-8 -*-
"""BeautifulNumber.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3ud2h97ah4PA_At-0PZ5dOkvTMuV2HH

#Beautiful Number

> You are given a number N. 

> A number is called beautiful if, for every digit x in the number, there are x occurrences of it in the number.

> Given the Number N return the next Beatiful Number

```
Example:
1 is beautiful because 1 has 1 occurrence. 
3133 is beautiful because 1 has 1 occurrence and 3 has 3 occurrences. 
224 is not beautiful because 4 does not have 4 occurrences. 
Find the smallest beautiful number which is greater than N

```
"""

def fact(n):
  facty=1
  for i in range(1,n+1):
    facty*=i

  return facty

def gimmeFactoftup(tup):
  facty=1
  for i in tup:
    facty*= fact(i)
  return facty

def gimmiGreaterThan(n,tup):

  if(len(tup)==1):
    return int(str(tup[0])*tup[0])
  
  stringy=""
  swappy=0
  swappyMain=1
  for i in tup:
    stringy+=str(i)*i

  zen= fact(len(stringy))/gimmeFactoftup(tup)
  
  while True:

    for i in range(len(stringy)-1):
      if (int(stringy)> n):
        break
    
      tempNumber=''
      a=list(stringy)
      if a[swappy]!=a[swappy+1]:
        a[swappy],a[swappy+1]=a[swappy+1],a[swappy]

        for digit in a :
          tempNumber+=digit

        stringy=tempNumber
        #print(stringy)
      swappy+=1
      swappyMain+=1

    if (int(stringy)> n or swappyMain>zen-1):
      break
    swappy=0
    
  return int(stringy) if n< int(stringy) else 99999999999999999999999999999999999999999

def beautifulNumber(n):
  refDict = {
      1:[(1,)],
      2:[(2,)],
      3:[(1,2),(3,)],
      4:[(1,3),(4,)],
      5:[(1,4),(2,3),(5,)],
      6:[(1,2,3),(1,5),(2,4),(6,)],
      7:[(1,2,4),(3,4),(2,5),(1,6),(7,)],
      8:[(1,2,5),(1,7),(2,6),(3,5),(4,4),(8,)],
      9:[(1,2,6),(1,3,5),(4,5),(3,6),(2,7),(1,8),(9,)],
      10:[(1,2,7),(1,3,6),(1,4,5),(5,2,3),(1,9),(2,8),(3,7),(4,6)],
      

  }
  leadingElement = int(str(n)[0])
  lengthOfn=len(str(n))
  k= lengthOfn if n<(int(str(lengthOfn)*lengthOfn)) else lengthOfn+1
  availableTuples=refDict[k]

  #print(availableTuples)
  eligibleTuples=[]
  if k==lengthOfn:
    for tup in availableTuples:
      for i in tup:
        if i>=leadingElement:
          eligibleTuples.append(tup)
          break
  else:
    eligibleTuples=availableTuples.copy()

  results=[]
  for tup in eligibleTuples:
    results.append(gimmiGreaterThan(n,tup))
  print(f'Available Tuples :  {availableTuples}')
  print(f'Eligible Tuples :  {eligibleTuples}')
  print(f'Eligible Results :  {(results)}')

  return min(results)

import time
start_time = time.time()
print(f'Result: {(beautifulNumber(int(901010101)))}')
print("\n\nElapsed Time :  %s seconds " % (time.time() - start_time))

def NormalButWeCheckBeautiful(n):
  listy = list(str(n))
  flag=True
  for i in listy:
    if listy.count(i)!=int(i):
      return not(flag)
  return flag

def NormalButBeautiful(n):
  notFound=True
  while (notFound):
    if NormalButWeCheckBeautiful(n):
      print(n)
      notFound=False
      break
    n+=1
  return n

import time
start_time = time.time()
print(f'Result: {(NormalButBeautiful(int(901010101)))}')
print("\n\nElapsed Time :  %s seconds " % (time.time() - start_time))