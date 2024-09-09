def NestedSum(nestedList):
    # Initialize the total sum to 0
    TotalSummen = 0
    # Iterate through each element in the nested list
    for object in nestedList:
        # If the element is a list, recursively call NestedSum
        if isinstance(object, list):
            TotalSummen += NestedSum(object)
        # If the element is not a list, add its value to the total sum
        else:
            TotalSummen += object
    # Return the total sum of all elements
    return TotalSummen


# Test Case 1: Nested lists with multiple levels
example_1 = [[[1, 2], [1, 2]], [[1, 2], [1, 2]]]
# Expected output: 12 (1+2+1+2+1+2+1+2)

# Test Case 2: Deeply nested single element
example_2 = [[[[[[[1]]]]]]]
# Expected output: 1

# Test Case 3: Mixed nested lists
example_3 = [[1, 2], [1, [1, 2], [1, 2, 3]], [1, [1, 2]]]
# Expected output: 17 (1+2+1+1+2+1+2+3+1+1+2)

# Print the results of the test cases
print(NestedSum(example_1))  # 12
print(NestedSum(example_2))  # 1
print(NestedSum(example_3))  # 17