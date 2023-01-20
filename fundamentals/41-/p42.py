def filter_list(l):

    list = []

    for arg in l:
        if str == type(arg):
            list.append(arg)
        
    for item_remove in list:
        l.remove(item_remove)
    return l
print(filter_list([2, 4, 5, 'sd', 'f']))