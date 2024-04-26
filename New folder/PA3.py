def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1, high - low


def quickSort(arr, low, high):
    if low < high:
        pivot_index, comparisons = partition(arr, low, high)
        comparisons_left = quickSort(arr, low, pivot_index - 1)
        comparisons_right = quickSort(arr, pivot_index + 1, high)
        return comparisons + comparisons_left + comparisons_right
    else:
        return 0


# Read input from the text file
with open("QuickSort.txt", "r") as file:
    input_array = [int(line.strip()) for line in file]

# Call the quickSort function and get the number of comparisons
total_comparisons = quickSort(input_array, 0, len(input_array) - 1)

# Print or return the total number of comparisons
print(total_comparisons)
