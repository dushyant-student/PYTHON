import json
p={"s":2,
   "p":"name",
   "d":"age",
   "w":{3,4,5}
        }
t=json.dumps(p)
j=t.read()
print(j)

#not work 