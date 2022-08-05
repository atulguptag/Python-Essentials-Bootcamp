'''Assignment - 3 
Remove the duplicate elements from the below list and maintain the order.
(Don't use sets)
'''
list1 = [1, 2, 3, 4, 1, 3, 1, 3, 100, 4, 1, 4]

list1 = list(dict.fromkeys(list1))

print(list1)

#Another way to remove duplicate elements from the list

another_list = [11, 13, 15, 16, 13, 15, 16, 11] 
print ("The list is: " + str(another_list)) 

# remove duplicated from list 
result = [] 
for i in another_list: 
    if i not in result: 
        result.append(i) 

# printing list after removal 
print ("The list after removing duplicates : " + str(result)) 