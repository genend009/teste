#include <stdio.h>
import random

print('hello world')
target = random.randint(1,1000)
print(target)

for i in range(1000):
    if i == target:
        print('線形探索法では',i,'番目にみつかりました')
        continue

hi = 1000
low = 1
mid = 500
t = 0
while (mid != target):
    if mid < target:
        low = mid + 1
    else:
        hi = mid - 1
    t = t + 1
    mid = (hi + low) / 2
    mid = int(mid)
    if low > hi:
        print('エラーです')
        break

        
if mid == target:
    print('二分探索法では',t,'番目にみつかりました') 



