'''
@author: Sarthak Pradhan

My implementation of merge sort algorithm for an array
'''
def split(array):
    #recursive function to split into two haves and merge

    if len(array)<=1: return array

    n = len(array)//2
    l = split(array[:n]) #left half of array
    r = split(array[n:]) #right half of array

    sort_list = merge(l,r)

    return sort_list 


def merge(l,r):
    #merges arrays after sorting them
    new_list = []
    i = 0
    j = 0
    while (i<len(l) and j<len(r)):
        if l[i]<=r[j]:
            new_list.append(l[i])
            i+=1

        else:
            new_list.append(r[j])
            j+=1
    if i<len(l):
        new_list.extend(l[i:])
    elif j<len(r):
        new_list.extend(r[j:])
    return new_list

#example case to test
a = [3,5,1,6,9,4,6,99,3,56,2]
print(a)
print(split(a))