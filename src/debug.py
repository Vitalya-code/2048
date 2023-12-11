from matrix import Matrix


# for i in range(5, 0, -1):
#     print(i)

matrix1 = Matrix(4, 4)
matrix1.spawn_new_cell(2)
matrix1.spawn_new_cell(2)
print("BEFORE")
matrix1.print()
matrix1.down()
print("AFTER")
# matrix1.print()
