n = int(input())
lst = []
countSwap = 0

for _ in range(n):
    ele = int(input())
    lst.append(ele)

for i in range(0, n-1):
    min_idx = i
    for j in range(i+1, n):
        if lst[j] < lst[min_idx]:
            min_idx = j
    if min_idx != i:
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        countSwap += 1


print(countSwap)
