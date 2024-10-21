'''
city = "ETLQALabs"
reverseString = city[ ::-1]
#print(reverseString)
substring =  city[ 3:8:1]
#print(substring)
list1 =[1,2,3,4,3]
list2 =[1,2,3,4]
if(len(list2)!=len(set(list2))):
    print("yes duplicate")
else:
    print("no not duplicate")

    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    oddIndex= list[1:10:2]
    print("odd index",oddIndex)
    evenIndex=list[0:9:2]
    print("even index", evenIndex)
'''
list1 = [2,4,4,5,6]
for i in range(2,8,2):
    print(i)