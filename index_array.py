def arr_index(arr, idx):
    return ''.join([el for sublist in arr for i, el in enumerate(sublist, start=1) if i in idx])

# Test cases
results1 = arr_index([['m', 'u', 'b'], ['a', 's', 'h'], ['i', 'r', '1']], [1, 3, 5, 8])
if results1 == 'mbsr':
    print("Test 1 passed!")
else:
    print(f"Test 1 failed! Expected 'mbsr', got {results1}")

results1 = arr_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9])
if results1 == 'myexample':
    print("Test 2 passed!")
else:
    print(f"Test 2 failed! Expected 'myexample', got {results1}")

results2 = arr_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6])
if results2 == 'mam':
    print("Test 3 passed!")
else:
    print(f"Test 3 failed! Expected 'mam', got {results2}")

results3 = arr_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8])
if results3 == 'mepl':
    print("Test 4 passed!")
else:
    print(f"Test 4 failed! Expected 'mepl', got {results3}")
