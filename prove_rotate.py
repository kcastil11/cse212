"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def rotate_list_right(data, ammount):
    final_list = []
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    # This add values to the final list
    for item in range(len(data) - ammount, len(data)):
        final_list.append(data[item])
 
    # This add the values before the final list
    # n to the end of final list
    for item in range(0, len(data) - ammount):
        final_list.append(data[item])
 
    return final_list
 
 


print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# # asks the number to rotate
# #check the len of the list
# rotate_num = 5
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
#output
# print(rotate_list_right(list, rotate_num))