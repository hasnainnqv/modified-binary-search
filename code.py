def modified_binary_search(data,item):
    data.sort()
    beg = 0
    end = len(data)-1
    mid = int((beg+end)/2)
    while beg<=end:
        mid = int((beg + end) / 2)
        if item<data[mid]:
            end = mid-1
        else:
            beg = mid+1
            
    if item == data[mid]:
        loc = mid
    else:
        if item<data[0]:
            data.insert(0,item)
            return "item not found in given list, item inserted at start of list"
        else:
            data.insert(-1,item)
            return "item not found in given list, inserted at the end of list "
    return loc
