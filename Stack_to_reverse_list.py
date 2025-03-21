def reverse_list(input_list):
    stack = []  #initializing stacks

    for items in input_list:
        stack.append(items)

    reverse_list = []
    while stack:
        reverse_list.append(stack.pop())
    return reverse_list

#example:

Sample_list = [2,3,4,5]
print("Original List: ", Sample_list)
print("Reversed_list:", reverse_list(Sample_list) )

