def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    if len(items)== 2:
        return f"{items[0]} and {items[1]}"
    if len(items) == 3:
        return f"{items[0]}, {items[1]}, and {items[2]}"
    else:
        return f"{', '.join(items[:-1])}, and {items[-1]}"
    

