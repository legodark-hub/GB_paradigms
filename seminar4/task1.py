def mean(values):
    return sum(values) / len(values)


def pearson_correlation(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Массивы должны иметь одинаковую длину")

    mean1, mean2 = mean(array1), mean(array2)

    covar = sum((array1[i] - mean1) * (array2[i] - mean2) for i in range(len(array1)))
    var1 = sum((x - mean1) ** 2 for x in array1)
    var2 = sum((y - mean2) ** 2 for y in array2)

    correlation_coefficient = covar / (var1**0.5 * var2**0.5)

    return correlation_coefficient
