## ORDENAR UN ARRAY ##
array = [46, 50, 65, 97, 69, 33, 59, 71, 98, 47, 55, 82, 35,  9, 75, 39, 93,
       11, 61, 94, 40, 73, 23, 92, 49, 76, 19,  8, 99, 70,  1, 66, 29, 28,
       45, 22, 27, 34, 54, 56, 63, 62, 78, 96, 10, 91,  4, 36, 32, 85, 90,
       95, 12, 48, 43, 53, 44, 51, 20,  7, 60, 77,  5, 18, 41, 13, 21, 87,
       17, 25, 67, 16, 57,  0, 72, 81, 84, 79, 38, 74, 52, 15,  6, 42, 64,
       89, 86, 68, 88, 14,  3, 30, 58, 80, 31, 37, 83, 24,  2, 26]
ordenacio = len(array)

for i in range(ordenacio):
    for j in range(0 , ordenacio - i - 1):
        if array[j] > array[j + 1]:
            # para comparar cual es mayor que el otro
            array[j] , array[j + 1] = array[j + 1] , array[j]
print(array)