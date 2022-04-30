def rotate_list_right(data, ammount):
    final_list = []
 
    # This add values to the final list
    for item in range(len(data) - ammount, len(data)):
        final_list.append(data[item])
 
    # This add the values before the final list
    # n to the end of final list
    for item in range(0, len(data) - ammount):
        final_list.append(data[item])
 
    return final_list
 
 
# asks the number to rotate
#check the len of the list
rotate_num = 5
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
#output
print(rotate_list_right(list, rotate_num))