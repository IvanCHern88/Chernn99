# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def repeats(a_list):
    repeat_dict = {key:0 for key in a_list}
    for key in a_list:
        repeat_dict[key] +=1
    return repeat_dict


print(repeats([1, 2, 3, 1, 4, 2, 2, 4, 6, 66, 454, 24, 5, 66, 4, 3]))
