#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    if len(my_list) > 0:
        new = my_list[0]
        for i in my_list:
            for j in my_list:
                if i != j:
                    new.append(i)
        return list(map((lambda x, y: x + y), new))
    return my_list

