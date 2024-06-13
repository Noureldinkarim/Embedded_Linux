
List = [0,1,4,2,3,4,4,4,5,6,7,8,4,9,10]
counter = 0
i=0

for i in range(len(List)):
    if List[i] == 4: counter = counter + 1
    else: pass

print(counter)