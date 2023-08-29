#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    array = []
    div = 0
    for el in range(list_length):
        try:
            div = my_list_1[el] / my_list_2[el]
        except IndexError:
            dix = 0
            print("out of range")
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        finally:
            array.append(div)
    return array
