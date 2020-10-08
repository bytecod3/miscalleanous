# calculate the sum of list elements recursively

def list_sum_recursive(input_list):
    # base case
    if input_list == []:
        return 0

    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


print(list_sum_recursive([7,8,0,2]))
