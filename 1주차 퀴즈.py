import itertools

num = [0] *7

def doit(n):
    global num
    num[n-1] = (num[n-1] + 1)%2

dice = list(range(1,5))

dice7 = [dice]*7

cases = itertools.product(*dice7)

all_case = 0

count = 0

for case in cases:
    num = [0] *7
    tmp = [doit(i) for i in case]
    print(num)

#         all_case +=1
#     case_1 = 0

#     for j in num:
#         if j == 1:
#             case_1 += 1

#     if case_1 == 1:
#         count += 1
 
# print(count/all_case)

