# 반복(for)

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

def selection_sort_for(my_list):
	for i in range(len(my_list)):
		min_idx = i
		for j in range(i + 1, len(my_list), 1):
			if my_list[j] < my_list[min_idx]:
				min_idx = j
		my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

selection_sort_for(my_list)
print(my_list)



################################################

# 재귀

def selection_sort_recursion(my_list, start, end):
    min_idx = start
    
    if start == end:
        return
    
    for j in range(start+1, end, 1):
        if my_list[j] < my_list[min_idx]:
            min_idx = j
    my_list[start], my_list[min_idx] = my_list[min_idx], my_list[start]
    selection_sort_recursion(my_list, start+1, end)


selection_sort_recursion(my_list, 0, 10)
print(my_list)