def top_k(lst, k):
    sort = []
    while lst and len(sort) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort