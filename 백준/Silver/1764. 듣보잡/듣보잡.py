#  듣보잡

N, M = map(int,input().split()) # N=듣도 못한, M=보도 못한 사람 수 
N_list = []
M_list = []
for NN in range(N):
    N_list.append(input())

for MM in range(M):
    M_list.append(input())

inter_set = set(N_list)&set(M_list)
inter_list = list(inter_set)
print(len(inter_set))
print(*sorted(inter_list))