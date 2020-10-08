# create a list recursively

def attach_head(element, input_list):
    return [element] + input_list

#  create list: [9,4,3,0]
print(attach_head(9,
            attach_head(4,
                        attach_head(3,
                                    attach_head(0, [])))))