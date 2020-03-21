# Josiah Burnham
# This Program preforms common matrix operations to solve math problems involving matrices

from operator import add, sub, mul, truediv


class CommonMatrixOperations:

    def __init__(self):
        # I got this idea from https://stackoverflow.com/questions/39552718/how-to-take-input-as-operation
        # creates a dictionary so that depending on the value of the operator variable it will use the correct function
        self.operations = {'*': mul, '/': truediv, '+': add, '-': sub}

    def matrix_add_sub(self, matrix, first_row, operator, second_row, row_to_apply):
        # this function adds two rows of a function together
        column = 0

        while column < len(matrix[first_row]):
            # see the stack overflow article in the init
            # adds the two elements together until the end of the row
            adj_element = self.operations[operator](matrix[first_row][column], matrix[second_row][column])
            matrix[row_to_apply].pop(column)
            matrix[row_to_apply].insert(column, adj_element)
            column += 1
        return matrix

    def matrix_mult_div_element(self, matrix, row, column, operator, row_to_mult):
        # this function multiplies entire rows of a matrix by a specific element
        specified_element = matrix[row][column]
        num = 0
        if specified_element == 0:
            # to avoid division by zero error
            pass

        else:
            if operator == '*':
                while num < len(matrix[row]):
                    # print(matrix[row_to_mult][num], end=operator) - DEBUG
                    # print(specified_element) - DEBUG

                    # You have to multiply the specified element with the opposite sign
                    # to the row that was already set to one has a one in the column
                    adj_element = self.operations[operator](matrix[row_to_mult][num], (specified_element * -1))
                    # W3 schools helped me find the pop() and insert() functions
                    # gets rid of the old element in the list
                    matrix[row_to_mult].pop(num)
                    # replaces the new element in its place
                    matrix[row_to_mult].insert(num, adj_element)

                    # adds one to move the index to pop and insert up by one
                    num += 1

                # you then add the row you just multiplied to the row with the specified element
                self.matrix_add_sub(matrix, row, '+', row_to_mult, row)
                # set the row you multiplied back to its original state per the rules of Gaussian elimination
                self.matrix_mult_div_element(matrix, row_to_mult, row_to_mult, '/', row_to_mult)

            else:
                while num < len(matrix[row]):
                    # print(matrix[row][num], end=operator) - DEBUG
                    # print(specified_element) - DEBUG

                    # please see the stack overflow article in the init
                    # dividing the specified element to the entire row that needs to be set have a one in the corner
                    adj_element = self.operations[operator](matrix[row][num], specified_element)
                    # W3 schools helped me find the pop() and insert() functions
                    # gets rid of the old element in the list
                    matrix[row].pop(num)
                    # replaces the new element in its place
                    matrix[row].insert(num, adj_element)

                    # adds one to move the index to pop and insert up by one
                    num += 1

            return matrix

    @staticmethod
    def usr_input(list, row, column):
        """
        DESCRIPTION:
         This function  oversees the user input and saving of that input into the matrix
        """

        print("Hello, please enter your  matrix below.\nPlease just make sure that"
              " the first element on the first row is not a zero\n\n")

        print("P.S This program loves going to a super high degree of precision\n so if a solution has a .9 repeating "
              "or a .0 repeating for 10 or so places it's safe to round to the nearest whole number.\n also"
              " please overlook the -0.0  that can happen from time to time.\n ")

        # saves the input into the correct places in the matrix
        for i in range(row):
            for x in range(column):
                list[i][x] = float(input(f"Please enter the [{i + 1}] [{x + 1}] element on the first row\n"))


class ReducedRowEchelon:
    def __init__(self):
        self.is_switched = False
        self.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def reducer(self):
        row_op = CommonMatrixOperations()
        row_op.usr_input(self.matrix, 3, 4)
        # to test if the last two rows were already switched
        if not self.is_switched:
            # sets the first thee elements down to Reduced Row Echelon for leaving the forth column as the answer
            row_op.matrix_mult_div_element(self.matrix, 0, 0, "/", 0)
            row_op.matrix_mult_div_element(self.matrix, 1, 0, "*", 0)
            row_op.matrix_mult_div_element(self.matrix, 2, 0, "*", 0)

            row_op.matrix_mult_div_element(self.matrix, 1, 1, "/", 1)
            row_op.matrix_mult_div_element(self.matrix, 0, 1, "*", 1)
            row_op.matrix_mult_div_element(self.matrix, 2, 1, "*", 1)

            row_op.matrix_mult_div_element(self.matrix, 2, 2, "/", 2)
            row_op.matrix_mult_div_element(self.matrix, 0, 2, "*", 2)
            row_op.matrix_mult_div_element(self.matrix, 1, 2, "*", 2)

            print("Your resulting matrix:")

            print("", self.matrix[0], "\n", self.matrix[1], "\n", self.matrix[2], "\n")

            choice = input('This is as far as I can take the matrix that you inputted as is.\n\nHowever if it\'s not '
                           'fully reduced, you may like to  switch the last two rows in your matrix\n'
                           ' which might help would you like me to do that? (Y/N) \n')

            if choice == "Y":
                self.is_switched = True
            else:
                print('Alright then, have a nice day!')

        if self.is_switched:
            # some matrices can not reduce right and it is necessary to switch the two rows to reduce more
            row_op.matrix_mult_div_element(self.matrix, 2, 1, "/", 2)
            row_op.matrix_mult_div_element(self.matrix, 0, 1, "*", 2)
            row_op.matrix_mult_div_element(self.matrix, 1, 1, "*", 2)

            row_op.matrix_mult_div_element(self.matrix, 1, 2, "/", 1)
            row_op.matrix_mult_div_element(self.matrix, 0, 2, "*", 1)
            row_op.matrix_mult_div_element(self.matrix, 2, 2, "*", 1)

            print('this is as far as i can take you matrix I\'m sorry if it is not what you are looking for')
            print("Your resulting matrix:")

            print("", self.matrix[0], "\n", self.matrix[1], "\n", self.matrix[2])


class InverseMatrix:
    def __init__(self):
        self.inverse_matrix = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]

    def find_inverse(self):
        # uses the methods from the CommonMatrix Operations class to find the inverse of the matrix
        row_op = CommonMatrixOperations()
        # gets user input
        row_op.usr_input(self.inverse_matrix, 3, 3)

        # reduces the first three elements down to Reduced Row Echelon form on one side with the identity on the other
        row_op.matrix_mult_div_element(self.inverse_matrix, 0, 0, "/", 0)
        row_op.matrix_mult_div_element(self.inverse_matrix, 1, 0, "*", 0)
        row_op.matrix_mult_div_element(self.inverse_matrix, 2, 0, "*", 0)

        row_op.matrix_mult_div_element(self.inverse_matrix, 1, 1, "/", 1)
        row_op.matrix_mult_div_element(self.inverse_matrix, 0, 1, "*", 1)
        row_op.matrix_mult_div_element(self.inverse_matrix, 2, 1, "*", 1)

        row_op.matrix_mult_div_element(self.inverse_matrix, 2, 2, "/", 2)
        row_op.matrix_mult_div_element(self.inverse_matrix, 0, 2, "*", 2)
        row_op.matrix_mult_div_element(self.inverse_matrix, 1, 2, "*", 2)

        print("Your resulting Inverse matrix:")

        print("", self.inverse_matrix[0], "\n", self.inverse_matrix[1], "\n", self.inverse_matrix[2])

        print('Please Remember that the inverse to your matrix is on the left side of the identity on the right')


def main():
    print("Hello, welcome to my matrix calculator")
    choice = int(input("For Gaussian Elimination(1), For finding the inverse of your matrix(2): "))
    print('\n')

    if choice == 1:
        ReducedRowEchelon().reducer()
    if choice == 2:
        InverseMatrix().find_inverse()


main()
