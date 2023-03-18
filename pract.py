# 4.Given an integer array, in-place reverse it without using any inbuilt functions.
#
# Input : [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# num = [1, 2, 3, 4, 5]
# temp=num[0]
# num[0]=num[4]
# num[4]=temp
# print(num)
# n = len(num)
# for i in range(int(n/2)):#
#     # temp=num[i] # temp=num[0]
    # num[i]=num[n-i-1] #num[0]=num[-1]
    # num[n-i-1]=temp #num[-1]=temp

    # num[i],num[n-i-1]=num[n-i-1],num[i]
    # num[i]=num[n-i-1]
    # temp=num[n-i-1]
# print(num)



# if __name__=='__main__':
# n=float(input('enter radius'))
# a=3.14*(n*n)
# print(a)

# first_name=input('enter 1st name')
# last_name=input('enter 2nd name')
# print(last_name+ " " + first_name)
#
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
# a=[1,2,3,3,5]
# def num(a):
#     for i in range(len(a)-1):
#         if a[i]!=a[i+1]:
#             return True
#
#     return False
# print(num(a))
#
a = [1, 2, 8, 3, 5]
def all_different(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
    return True

print(all_different(a))
