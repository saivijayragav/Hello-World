def magic_square(n, matrix):

    value, value2, value3, value4 = 0, 0, 0, 0
    h = n
    list1 = []
    list2 = []
    register = True
    register2 = True

    for i in range(n):

        value2 += matrix[i][i]
        value4 += matrix[i][h - 1]
        h -= 1

        for f in range(n):

            value += matrix[i][f]
            value3 += matrix[f][i]
        list1.append(value)
        list2.append(value3)
        value = 0
        value3 = 0

    for i in list1:

        if list1.count(i) == n:
            register = True
        else:
            register = False
    for f in list2:
        if list2.count(f) == n:
            register2 = True
        else:
            register2 = False
    if register == register2 == True:
        return 'Magic Square!'
    else:
        return 'Not a Magic Square!'


n = int(input())
mat = []
for r in range(n):
    nums = input()
    mat.append([int(x) for x in nums.split()])
print(magic_square(n, mat))
