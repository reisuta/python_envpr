N = int(input())
A = sorted(input().split())

list = []

for i in range(N):
  list.append(i+1)

for i in range(N):
  if int(A[i]) != list[i]:
    print('No')
    exit()

if N != len(A):
  print('No')
  exit()
    
print('Yes')