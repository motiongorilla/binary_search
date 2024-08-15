arr = [0,3,4,6,10,14,25,33,35,65,89,92,95,96,97,102]
to_search = 65
words = ["money", "bank", "nivea", "memes", "yegor", "nikita", "often", "beautiful", "exclamation", "ide", "yes", "no"]
s = "often"
i_found = None

def binary_search(arr: list, i_found, to_search):
    arr.sort()
    lo = 0
    hi = len(arr)-1
    while i_found is None:
        mid = (lo+hi)//2
        if lo == hi and arr[lo] != to_search:
            return print("Element is not in this list")

        if arr[mid] == to_search:
            i_found = mid
            return print(f"Found! It's {to_search} at index {i_found}. Check this {arr[i_found]}")

        if arr[mid] > to_search:
            hi = mid-1
        
        if arr[mid] < to_search:
            lo = mid+1

f_ind = 0
l_ind = len(arr)-1
def binary_search_recur(arr, i_found, to_search, low, high):
    lo = low
    hi = high
    mid = (lo+hi)//2
    if lo == hi and arr[lo] != to_search:
        return print("Element is not in this list")

    if arr[mid] == to_search:
        i_found = mid
        return print(f"Found! It's {to_search} at index {i_found}. Check this {arr[i_found]}")

    if arr[mid] > to_search:
        hi = mid-1
        binary_search_recur(arr, i_found, to_search, lo, hi)
    
    if arr[mid] < to_search:
        lo = mid+1
        binary_search_recur(arr, i_found, to_search, lo, hi)

binary_search(words, i_found, s)
# binary_search_recur(arr, i_found, to_search, f_ind, l_ind)