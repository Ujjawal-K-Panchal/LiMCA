def top_k(lst, k):
    new_list = []
    while len(new_list) < k:
        maximum = max(lst)
        new_list.append(maximum)
        lst.remove(maximum)

    return new_list