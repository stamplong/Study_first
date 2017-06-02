import shutil
import os
import time
import re
for a,b,c in os.walk('/Users/admin/Study_first',topdown = True,onerror = None):
    print a

abc = os.listdir('/Users/admin/Study_first')
mo = re.compile(r'\d*\.txt')
for i in abc:
    abc1 = mo.findall(i)
    for x in abc1:
        if x!=None:
            print x
            f = os.path.join('/Users/admin/Study_first',x)
            d = time.strftime('%H-%M-%S')
            c = d  + ".txt"
            shutil.move(f,c)
            time.sleep(2)
