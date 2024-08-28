def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count(arr[:mid])
    right, inv_right = merge_sort_and_count(arr[mid:])
    merged, inv_merge = merge_and_count(left, right)
    
    return merged, inv_left + inv_right + inv_merge

def merge_and_count(left, right):
    merged = []
    inv_count = 0
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count

def count_inversions(arr):
    _, inv_count = merge_sort_and_count(arr)
    return inv_count

def compare_preferences(viewer1, viewer2):
    # Create a mapping of movies to their indices in viewer1's list
    movie_to_index = {movie: i for i, movie in enumerate(viewer1)}
    
    # Convert viewer2's list to indices based on viewer1's order
    viewer2_indices = [movie_to_index[movie] for movie in viewer2]
    
    # Count inversions in viewer2_indices
    inversions = count_inversions(viewer2_indices)
    
    return inversions

# Example usage
viewer1 = ['Shrek', 'Star Wars', 'Pirates of the Caribbean', 'The Imitation Game']
viewer2 = ['Star Wars', 'The Imitation Game', 'Shrek', 'Pirates of the Caribbean']

difference = compare_preferences(viewer1, viewer2)
print(f"The number of inversions (differences in preference) is: {difference}")
