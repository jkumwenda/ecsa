def flatten_array(arr):
    data = []
    for item in arr:
        if isinstance(item, list):
            data.extend(flatten_array(item))
        else:
            data.append(item)
    return data


# Example usage:
nested_array = [1, [2, 3], [[4], [5]]]
flattened_array = flatten_array(nested_array)
print(flattened_array)
