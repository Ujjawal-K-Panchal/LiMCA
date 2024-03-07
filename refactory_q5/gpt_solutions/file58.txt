def top_k(lst, k):
    new_lst = []
    for i in range(k):
        max_value = max(lst)
        new_lst.append(max_value)
        lst.remove(max_value)
    return new_lst