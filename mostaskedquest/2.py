dict1 = {100:'Sachin',70:'kohli',32:'SharmaJi'}


dict2 = {k:v for k,v in sorted(dict1.items(),key=lambda x:x[0])}

print(dict2)