grade = {'A+': 4.5,
         'A0': 4.0,
         'B+': 3.5,
         'B0': 3.0,
         'C+': 2.5,
         'C0': 2.0,
         'D+': 1.5,
         'D0': 1.0,
         'F': 0.0}

C_sum = 0
CG = 0
for _ in range(20):
    l, C, G = input().split()
    c = float(C)
    if str(G) != 'P':
        CG += c*grade[G]
        C_sum += c
    else:
        pass
print('%.6f' % (CG/C_sum))