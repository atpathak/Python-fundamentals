def variance(numbers):
    length = len(numbers)
    mean = sum(numbers) / length
    square_differences_from_mean = []
    for number in numbers:
        square_differences_from_mean.append((number - mean) ** 2)
    sum_of_square_differences = sum(square_differences_from_mean)
    variance = sum_of_square_differences / length
    return variance

var = variance([2,4,5,10,14])
print(var)

