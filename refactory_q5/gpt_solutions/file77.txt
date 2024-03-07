def top_k(lst, k):
    result = []
    while lst:
        maximum = lst[0]  # arbitrary number in list 
        for x in lst: 
            if x > maximum:
                maximum = x
        result.append(maximum)
        lst.remove(maximum) 
    return result[:k]