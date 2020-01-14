# author:Yitian Chen time:2020/1/14
'''ln(6)'''
a1 =[1,2,3,4]
sum =0
for i in a1:
    for j in a1:
        for k in a1:
            if i!=j and j!=k:
                print(i,j,k)
                sum+=1

'''ln(8)'''
print(sum)
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, [1, 2, 7,12,45,56,66])))
