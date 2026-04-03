import sys
sys.stdin = open("input.txt")

N = int(input())
Pi = list(map(int, input().split()))

Pi.sort()
# print(Pi)
sum = 0

for i in range(len(Pi)):
    sum += Pi[i] * (len(Pi) - i)

print(sum)