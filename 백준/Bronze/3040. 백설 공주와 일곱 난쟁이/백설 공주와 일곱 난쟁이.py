# 난쟁이 문제 , 런타임 오류
dwarf =[]               
for _ in range(9):      
    one = int(input())
    dwarf.append(one) 
for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarf)- (dwarf[i]+dwarf[j]) ==100:
            f1,f2= i,j
            break
dwarf.pop(f1)
dwarf.pop(f2-1)
           
print(*dwarf, sep='\n')