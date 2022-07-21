def solution(n, m):
    i = 0
    while True:
        i += 1
        if (n%i) == 0 and (m%i) == 0:
            return solution(n/i, m/i)
        else:
            break

print(solution(3, 12))