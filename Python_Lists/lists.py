# Step 1: Create an empty list called my_list. 
my_list = []
print(f"1. Initially, my_list is: {my_list}")

# Step 2: Append the following elements to my_list: 10, 20, 30, 40. 
# The append() method adds one element at a time to the end of the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"2. After appending: {my_list}")

# Step 3: Insert the value 15 at the second position in the list. 
# The insert() method takes two arguments: insert(index, value).
# The "second position" corresponds to index 1 (since list indices start at 0).
my_list.insert(1, 15)
print(f"3. After inserting 15 at index 1: {my_list}")

# Step 4: Extend my_list with another list: [50, 60, 70]. 
# The extend() method adds all elements from another list to the end.
extension_list = [50, 60, 70]
my_list.extend(extension_list)
print(f"4. After extending with {extension_list}: {my_list}")

# Step 5: Remove the last element from my_list. 
# The pop() method removes and returns the last item if no index is specified.
removed_element = my_list.pop()
print(f"5. After removing the last element ({removed_element}): {my_list}")

# Step 6: Sort my_list in ascending order. 
# The sort() method sorts the list in-place (it modifies the original list).
my_list.sort()
print(f"6. After sorting: {my_list}")

# Step 7: Find and print the index of the value 30 in my_list. 
# The index() method returns the index of the first occurrence of a value.
index_of_30 = my_list.index(30)
print("\n--- Final Step ---")
print(f"7. The index of the value 30 in the final list is: {index_of_30}")