#!/usr/bin/python3
flatten_list=[]
def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''


    for element in aList:
        if type(element) is list:
            print('ecco')
            flatten(element)
        else:
            flatten_list.append(element)

    return flatten_list

ali = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


print(flatten(ali))
