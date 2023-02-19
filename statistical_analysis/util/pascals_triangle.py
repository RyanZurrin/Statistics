from pprint import pprint


def pascals_triangle(n, display=True):
    """Returns the first n rows of Pascal's triangle as a list of lists."""
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, n):
            result.append([1] + [result[i - 1][j] + result[i - 1][j + 1] for j in range(i - 1)] + [1])
        if display:
            for row in result:
                print('  ' * (n - len(row)), end='')
                pprint(row)

        return result
