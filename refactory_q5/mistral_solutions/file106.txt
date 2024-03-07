def top_k(lst, k):
    new = []
    lst.sort(reverse=True)
    for i in range(k):
        new.append(lst[i])
    return new