class Matrix:
    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns
        # create a matrix
        self.__matrix = []
        self.__matrix.append([2, 0, 0, 2])
        self.__matrix.append([0, 0, 0, 0])
        self.__matrix.append([0, 2, 0, 0])
        self.__matrix.append([0, 0, 2, 0])

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

    def spawn_new_cell(self):
        random_cell = self.get_random_cell()
        if random_cell is False:
            return False

        self.set(SPAWN_CELL_VALUE, random_cell[0], random_cell[1])
        return True

    def left(self):
        # this is super complicated, good luck
        rows = self.__rows
        columns = self.__columns
        # we iterate through each element in the matrix
        for x in range(0, columns):
            for y in range(0, rows):
                if self.get(x, y) != 0:
                    move_to = x
                    old_value = self.get(x, y)
                    while move_to > 0:
                        move_to = move_to - 1
                        print(move_to)
                        if self.get(move_to, y) != 0:
                            move_to = move_to + 1
                            break

                    self.set(old_value, move_to, y)
                    self.set(0, x, y)