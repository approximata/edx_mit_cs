
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    temp_increasing = []
    temp_decreasing = []
    increaseing = []
    decreaseing = []

    first_increased = 0
    first_decreased = 0
    final_increased = 0
    final_decreased = 0

    i = 0
    while i < len(L)-1:

        while i < len(L)-1 and L[i+1] <= L[i]:
            temp_increasing.append(L[i])
            i += 1
        else:
            temp_increasing.append(L[i])
            first_increased = i

        if len(temp_increasing) > len(increaseing):
            increaseing = temp_increasing[:]
            final_increased = first_increased

        temp_increasing = []
        i += 1


    i = 0
    while i < len(L)-1:

        while i < len(L)-1 and L[i+1] >= L[i]:
            temp_decreasing.append(L[i])
            i += 1
        else:
            temp_decreasing.append(L[i])
            first_decreased = i


        if len(temp_decreasing) > len(decreaseing):
            decreaseing = temp_decreasing[:]
            final_decreased = first_decreased

        temp_decreasing = []
        i += 1

    if len(decreaseing) > len(increaseing):
        print(decreaseing, 'simadec')
        return sum(decreaseing)
    elif len(decreaseing) < len(increaseing):
        print(increaseing, 'simainc')
        return sum(increaseing)
    else:
        if final_decreased > final_increased:
            print(increaseing, 'egyeninc')
            return sum(increaseing)
        else:
            print(decreaseing, 'egyendec')
            return sum(decreaseing)



cucc = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
cucc2 = [5, 4, 10]
cucc3 = [1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5]
cucc4 = [1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(longest_run(cucc4))
