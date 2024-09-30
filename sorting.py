def bubble(bubble_list):
    length = len(bubble_list)
    times = 0
    for x in range(length):
        times += 1
        sorted = True
        for y in range(length-x-1):
            if bubble_list[y] > bubble_list[y+1]:
                keep = bubble_list[y]
                bubble_list[y] = bubble_list[y+1]
                bubble_list[y+1] = keep
                sorted = False
        if sorted == True:
            break
    print(times)
    return bubble_list

def selection(selection_list):
    length = len(selection_list)
    for x in range(length):
        min = selection_list[x]
        location = x
        for y in range(length - x):
            if min > selection_list[y+x]:
                min = selection_list[y+x]
                location = y+x
        selection_list[location] = selection_list[x]
        selection_list[x] = min
    return selection_list

def insertion(insertion_list):
    length = len(insertion_list)
    for x in range(length):
        y = x
        while y > 0:
            if insertion_list[y] < insertion_list[y-1]:
                keep = insertion_list[y]
                insertion_list[y] = insertion_list[y-1] 
                insertion_list[y-1] = keep
            else:
                break
            y -= 1
    return insertion_list
