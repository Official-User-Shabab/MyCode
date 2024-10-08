def cleanNsort(mixed):
    cleaned = []
    # Looping through mixed list
    for item in mixed:
        if isinstance(item, int):
            cleaned.append(item)
    cleaned.sort()
    return cleaned

# Put your array here
mixed = [1, "lkoj", 2, 3, "fvfva", 5, "rwf", 4]
doneList = cleanNsort(mixed)
print(doneList)
