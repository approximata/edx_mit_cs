#!/usr/bin/python3

def flatten(aList):
    flatten_list=[]
    def reflat(anylist):
        for element in anylist:
            if type(element) is list:
                reflat(element)
            else:
                flatten_list.append(element)

        return flatten_list

    return reflat(aList)

ali = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
ali2 = [[1]]
ali3 = [[1], [1]]
ali4 = [[1], [2, 3]]

print(flatten(ali))
