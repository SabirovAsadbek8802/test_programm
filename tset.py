import json

d={
    "savollar":{

    }
}

file=open('data_base.txt','r',encoding="utf8")
data=file.readlines()
t = 0
for i in range(0,len(data),5):
    t+=1
    a={
        f"savol{t}":{
            "savol":data[i],
             "javoblar":{
                 data[i+1]:"A",
                 data[i+2]:"B",
                 data[i+3]:"C",
                 data[i+4]:"D",
             },
            "tj":data[i+1]
        }
    }
    d['savollar'].update(a)

dd=json.dumps(d)
print(dd)