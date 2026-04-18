def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result
students = [[1, 'Alice', 'IV'], [2, 'Bob', 'VI'], [3, 'Charlie', 'III'], [4, 'Vihaan', 'VII'], [5, 'Jayanth', 'VIII  ']]

print(test(students))
