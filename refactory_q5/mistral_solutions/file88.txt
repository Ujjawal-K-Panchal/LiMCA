def top_k(lst, k):
    lst = sorted(lst, reverse=True)
    return lst[:k]