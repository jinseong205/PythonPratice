def recursive_function(i):
    if i == 100:
        return
    print("recursive function : ",i)
    recursive_function(i+1)

recursive_function(1)