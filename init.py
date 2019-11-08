import os
import json
import re
_l1=os.listdir("json/") #reading all json files with data in json folder

_l1=[os.path.abspath("json/"+i) for i in _l1] #list of absolute path of json files in json folder

_org=[]
for i in _l1:
   
    if i.split(".")[1]=="json": #checking json file or not (suffix-check)
        
        
        _org.append(i)
#print(_org)
mk1={}
for i in _org:
    f1=open(i,'r')
    r1=json.loads(f1.read()) #reading the file (json loads)
    f1.close()
    for j in r1:
        mk1[j]=[] #making key pair pattern,if more than one same key or array/list exist (employee/cricketer/striker) then it will merge them in one
for i in _org:
    f1=open(i,'r')
    r1=json.loads(f1.read())
    f1.close()
    for _j in r1:
        for _k in r1[_j]:
            mk1[_j].append(_k)

l2=os.listdir()
mx_merge=0
for i in l2:
    _s=i.split(".")
    try:
        
        if _s[1]=="json":
            _t=_s[0]
            _o=_t[::-1][0]
           
            _o=int(_o)
            if mx_merge<_o:
                mx_merge=_o
            
           
    except:
        pass
new_merge_file="merger"+str(mx_merge+1)+".json" #every time new merger.json will be created with one incremented value (In sequence)
with open(new_merge_file,'w+',encoding='utf-8') as f1:
    json.dump(mk1,f1,ensure_ascii=True,indent=4) 
    
    
f1.close()       
for i in mk1:
    print(i,mk1[i])
    print("------------------------")