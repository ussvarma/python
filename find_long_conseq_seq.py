""" To find the longest consecutive increasing or decreasing subsequence
      and its summation """

sequence = list(map(int, input("enter space separated numbers: ").split()))
len_list = len(sequence)

long_conseq_incre_list = []  # declaring in global scope
long_conseq_decre_list = []  # declaring in global scope

for i in range(len_list):  # updates long_conseq_incre_list
    inner_list = []        # declaring inner_list in local scope
    for j in range(i, len_list - 1):
        if sequence[j] <= sequence[j + 1]:
            inner_list.append(sequence[j])
        else:
            break
    if (sequence[-2] <= sequence[-1]) \
            and sequence[j] == sequence[-2]:
        inner_list.append(sequence[-1])
    else:
        inner_list.append(sequence[j])
    if len(inner_list) > len(long_conseq_incre_list) and len(inner_list) > 1:
        long_conseq_incre_list = inner_list

for i in range(len_list):  # updates long_conseq_decre_list
    inner_list = []         # declaring inner_list in local scope
    for j in range(i, len_list - 1):
        if sequence[j] >= sequence[j + 1]:
            inner_list.append(sequence[j])
        else:
            break
    if (sequence[-2] >= sequence[-1]) and sequence[j] == sequence[-2]:
        inner_list.append(sequence[-1])
    else:
        inner_list.append(sequence[j])
    if (len(inner_list) > len(long_conseq_decre_list)) and len(inner_list) > 1:
        long_conseq_decre_list = inner_list


def sum_long_sequence(long_conseq_incre_list,
                      long_conseq_decre_list):
    """  prints the sum of the longest sequence """

    if len(long_conseq_incre_list) < len(long_conseq_decre_list):
        return sum(long_conseq_decre_list)
    elif len(long_conseq_incre_list) > len(long_conseq_decre_list):
        return sum(long_conseq_incre_list)
    else:
        if long_conseq_incre_list.index(long_conseq_incre_list[0]) \
                < long_conseq_decre_list.index(long_conseq_decre_list[0]):
            return sum(long_conseq_incre_list)
        else:
            return sum(long_conseq_decre_list)


print("long_conseq_incre_list: ", long_conseq_incre_list)
print("sum of elements: ",
      sum_long_sequence(long_conseq_incre_list, long_conseq_decre_list))