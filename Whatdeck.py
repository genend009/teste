#include <stdio.h>
import random

print('hello world')

list = [0] * 100 #デッキ選択
for i in range(100):
 n = random.randint(1,1000)
 list[i] = 1200
 if(n <= 300):
  list[i]=1100
  continue
 if(n <= 600):
  list[i] = 1300
for i in range (0,100,1):
 print(list[i])
print(len(list))
    


