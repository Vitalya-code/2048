import random


class Matrix:
    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns
        self.__score = 0

        # create a matrix
        self.__matrix = []
        self.__matrix.append([0, 0, 0, 0])
        self.__matrix.append([0, 0, 0, 0])
        self.__matrix.append([0, 0, 0, 0])
        self.__matrix.append([0, 0, 0, 0])

    def get_score(self):
        return self.__score

    def get_matrix(self):
        return self.__matrix

    def print(self):
        for i in self.__matrix:
            print(i)

    def set(self, value: int, x: int, y: int):
        self.__matrix[y][x] = value

    def get(self, x: int, y: int):
        if x < 0 or y < 0:
            return False
        return self.__matrix[y][x]

    def get_random_cell(self):
        # returns position of one random free cell
        possible_cells = []
        for count_y, y in enumerate(self.__matrix):
            for count_x, x in enumerate(y):
                if x == 0:
                    possible_cells.append([count_x, count_y])
        # no free space
        if len(possible_cells) <= 0:
            return False

        return random.choice(possible_cells)

    def spawn_new_cell(self, value):
        random_cell = self.get_random_cell()
        if random_cell is False:
            return False

        self.set(value, random_cell[0], random_cell[1])
        return True

    def move_and_merge(self, row):
        merged = row

        for x, value in enumerate(row):
            for i in range(x, 0, -1):
                if row[i - 1] == 0:
                    merged[i - 1] = value
                    merged[i] = 0
                elif row[i - 1] != 0:
                    if row[i - 1] == row[i]:
                        merged[i - 1] = merged[i - 1] * 2
                        merged[i] = 0
                        self.__score = self.__score + merged[i - 1]

                        break
                    break

        return merged

    def flip_matrix_horizontally(self, matrix):
        # borrowed from internet
        return [row[::-1] for row in matrix]

    def flip_matrix_vertically(self, matrix):
        # borrowed from internet
        return matrix[::-1]

    def rotate_right(self, matrix, times=1):
        # borrowed from internet
        for _ in range(0, times):
            transposed_matrix = [list(row) for row in zip(*matrix)]
            matrix = [row[::-1] for row in transposed_matrix]

        return matrix

    def left(self):
        for i, row in enumerate(self.__matrix):
            new_row = self.move_and_merge(row)
            self.__matrix[i] = new_row

    def right(self):
        # instead of doing another function, we just flip
        # the matrix horizontally and reuse the old code
        # and then flip it again

        self.__matrix = self.flip_matrix_horizontally(self.__matrix)
        for i, row in enumerate(self.__matrix):
            new_row = self.move_and_merge(row)
            self.__matrix[i] = new_row
        self.__matrix = self.flip_matrix_horizontally(self.__matrix)

    def up(self):
        self.__matrix = self.rotate_right(self.__matrix, 3)
        for i, row in enumerate(self.__matrix):
            new_row = self.move_and_merge(row)
            self.__matrix[i] = new_row
        self.__matrix = self.rotate_right(self.__matrix)

    def down(self):
        self.__matrix = self.rotate_right(self.__matrix)
        for i, row in enumerate(self.__matrix):
            new_row = self.move_and_merge(row)
            self.__matrix[i] = new_row
        self.__matrix = self.rotate_right(self.__matrix, 3)
