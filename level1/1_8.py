'''
최대공약수와 최소공배수

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
'''

# def solution(n, m):
#     answer = []

#     return answer

n = 3
m = 12
max_n = []
max_m = []
min_n = []
min_m = []
gop = 1
j = 1
y = 1

for i in range(1, n+1):
    if (n%i) == 0:
        max_n.append(i)
        i += 1
while True:
    gop = j*n
    min_n.append(gop)
    j += 1
    if gop >= 100:
        break
    

for x in range(1, m+1):
    if (m%x) == 0:
        max_m.append(x)
        x += 1
while True:
    gop = y*m
    min_m.append(gop)
    y += 1
    if gop >= 100:
        break

print(max_n)
print(min_n)
print(max_m)
print(min_m)