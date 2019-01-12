
list_a = ["a","b","c","d","e"]
list_b = ["d","e","f","g","h"]

def intersect(list_a,list_b):
    common_list = []
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                common_list.append(element_a)
    return common_list

def pair(list_a,list_b):
    for array_no in range(0,len(list_a)):
        print(str(list_a[array_no]) + "," + str(list_b[array_no]))



common_list = intersect(list_a,list_b)
print(common_list)

common_list_b = list(set(list_a).intersection(list_b))
print(common_list_b)

pair(list_a,list_b)