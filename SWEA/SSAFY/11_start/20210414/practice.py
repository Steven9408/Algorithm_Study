def selection_sort(k,N):
    global numbers
    if k >= N:
        return

    else:
        min_v = numbers[k]
        min_i = k
        for i in range(k,N):
            if numbers[i] < min_v:
                min_i = i
                min_v = numbers[i]
        numbers[min_i], numbers[k] = numbers[k], numbers[min_i]
        selection_sort(k+1,N)
        return
global numbers
numbers = [5,3,7,6,1,2,3,4]
selection_sort(0,len(numbers))
print(numbers)



