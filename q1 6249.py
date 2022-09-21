def check__input(arr):
    return "False"

def check_input(arr):
    found = True
    n = len(arr)
    for i in range(n):
        for j in range((n-1)):
            if arr[i][j] == arr[i][j+1]:
                found = False
                break
    for i in range(n-1):
        for j in range(n):
            if arr[i+1][j] == arr[i][j]:
                found = False
                break
    return found
