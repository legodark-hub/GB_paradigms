def sort_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
def sort_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers
