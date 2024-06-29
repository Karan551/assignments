def plusMinusArr(arr):
    length_ar = len(arr)
    positive_number_lst = []
    negative_number_lst = []
    for i in arr:
        if i > 0:
            positive_number_lst.append(i)
        elif i < 0:
            negative_number_lst.append(i)

    rem = length_ar - (len(positive_number_lst) + len(negative_number_lst))

    print(len(positive_number_lst) / length_ar)
    print(format(len(positive_number_lst) / length_ar, ".6f"))
    print()
    print(len(negative_number_lst) / length_ar)
    print(format(len(negative_number_lst) / length_ar, ".6f"))
    print()
    print(rem / length_ar)
    print(format(rem / length_ar, ".6f"))


lst = [-4, 3, -9, 0, 4, 1]
plusMinusArr(lst)
