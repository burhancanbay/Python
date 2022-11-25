# data=1
# while data<=10:
#     print(data)
#     data=data+1

# data=[1,2,0,5,10]
# a=1
# for x in data:
#     if x==0:
#         continue
#     a=a*x
# print('The value of a is {}'.format(a))

data=[1,2,0,5,10]
search=0
for x in data:
    if x==search:
        print('Value is found')
        break