def find_largest_element(lst):
    if not lst:
        return None
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

my_list = [12, 45, 74, 23, 98, 56]
largest = find_largest_element(my_list)
print(f"The largest element in the list is {largest}")


a,b=input().split()
print(max(int(a),int(b)))

