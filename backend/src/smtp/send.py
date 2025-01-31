# k = int(input())
# m = [int(i) for i in input().split()]
# if k == 1: print(abs(sorted(m)[-2]-sorted(m)[-3]-sorted(m)[-4]))
# else: print(min(m))

# res = []
# n = int(input())
# m = [input() for i in range(n)]
# list = [i.count('C') for i in m]
# for s in range(len(m)):
#     for r in range(len(m[s])):
#           print(m[s][r])
#     # if m[s].count('C') == 0:
#     #         print(m[s])
#     #         m[s] = '1' * n  

        
# print(m)
# def binarysearch(a,s):
#     if a *2 >s:
#         a = a*2
#         binarysearch(a,s)
#     if a * 2 < s:
#         a = round(a/s)+1
#         binarysearch(a,s)
#     if a == s:
#         print(a)
# binarysearch(14, 112)

# k = 0
# res = []
# s = int(input())
# r = 0
# def beautifulnum(num):
#     for i in range(len(str(num))-1):
#         if str(num)[i] == str(num)[i+1]:
#             return False
#     return True
# ran = '0' * (len(str(s))-1)
# if s <= int('1'+ran)*2:
#     print(0)
# if s > int('1'+ran)*2:
#     for i in range(int('1'+ran), int('1'+ran)*10):
#         for j in range(int('1'+ran), int('1'+ran)*10):
#             if i + j == s:
#                 if beautifulnum(i) and beautifulnum(j):
#                     res.append(i)
#                     res.append(j)


#     print(int(len(res)/2))
result = []
res = []
m = [int(i) for i in input().split()]
l = [input() for f in range(m[0])]
for row in l:
    res = [i for i in row]
    for liter in range(3):
        if row[liter] != row[liter * -1 - 1]:
            if row[liter] == 'x':
                if m[-1] > 0:
                    m[-1] = m[-1]-1
                    res[liter * -1 -1] = 'x'
            else:
                if m[-1] > 0:
                    m[-1] = m[-1]-1
                    res[liter] = 'x'
            
    result.append(''.join(res))
print(res)
for i in result:
    print(i)

# m = [int(i) for i in input().split()]
# res = []
# boys = m[0]
# girls = m[-1]
# for i in range(boys):
#     res.append('B')
    
#     if girls>0:
#         res.append('G')
#     else:
#         if boys > 0:
#             res.append('B')
#     if girls > 0:
#         res.append('G')
#     else:
#         if boys > 0:
#               res.append('B')
#     boys = boys-1  
# print(res[:sum(m)])

    