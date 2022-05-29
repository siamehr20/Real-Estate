import json
import os

# test= {'name': 'Siavsh' , 'lastname' : 'Rad' , 'age': 21 }
# jtest = json.dumps(test)
# print(jtest)

with open('D:\projects\Estate Project\siamehr.txt' , 'r') as f:

    line = f.read()
    agents_list = json.loads(line)
print(agents_list[1])
    # f.writelines('second line')
    # print(f.readlines())
      
