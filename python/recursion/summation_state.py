def summation(current_number, accumulated_sum):
    # base case
    # return the final state
    if current_number == 11:
        return accumulated_sum

    # recursive case
    # thread the state through the recursive call
    else:
        return summation(current_number + 1, accumulated_sum + current_number)


if __name__ == '__main__':
    #  pass the initial state
    print(summation(1, 0))