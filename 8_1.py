import random
import os
capitals = {'hunan':'changsha','beijing':'beijing','jiangxi':'nanchang','hubei':'wuhan','zhongguo':'china','hujian':'xiamen',
"guangzhou":'shenzheng','taiwang':"taibei"}

dic_keys = capitals.keys()
dic_values = capitals.values()
path = os.getcwd()
if os.path.exists("/Users/admin/Study_first/papers")==False:
    os.makedirs('/Users/admin/Study_first/papers')
else:
    pass
for quizNum in range(6):
    quizfile = open('/Users/admin/Study_first/papers/capitals%s.txt'%(quizNum+1),'w')
    quizfile.write('Name:\nDate:\n')
    quizfile.write((' '*20)+'State capitals quiz (from %s)'%(quizNum+1))
    quizfile.write("\n\n")
for x in range(5):
    random.shuffle(dic_keys)
    random.shuffle(dic_values)
    Answer = []
    print dic_values
    for x in dic_values:
        if(len(Answer)<3):
            Answer.append(x)
        else:
            break
    for index in range(5):
        Answer.append(dic_keys[index])
        if(len(Answer)>4):
            del Answer[3]
        random.shuffle(Answer)
        print Answer
