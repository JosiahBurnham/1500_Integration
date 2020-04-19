# Josiah Burnham
# https://github.com/JosiahBurnham/1500_Integration
"""
This Program preforms common matrix operations
to solve math problems involving matrices

"""
from typing import Any

from operator import add, sub, mul, truediv


class CommonMatrixOperations:
    """
    This class contains common matrix operations that are used by other
    classes in the project.
    """

    def __init__(self):
        # I got this idea from https://stackoverflow.com/questions/39552718
        # creates a dictionary so that depending on the value of the
        # operator variable it will use the correct function
        self.operations = {'*': mul, '/': truediv, '+': add, '-': sub}

    def matrix_add_sub(self, matrix, first_row, operator, second_row,
                       row_to_apply):
        """
        this function adds or subtracts rows of a given matrix and applies
        the operation to one of the two rows

        :param matrix: the list of lists that needs to be added or subtracted
        :param first_row: the first row that needs to be added to or
               subtracted from
        :param operator: a string that contains the operation that is desired
        :param second_row: the row that is added or taken away form the first
        :param row_to_apply: the row that needs to be adjusted
        :return: the adjusted matrix with the desired operations preformed
        """
        column = 0

        while column < len(matrix[first_row]):
            # see the stack overflow article in the init
            # adds the two elements together until the end of the row
            adj_element = self.operations[operator](matrix[first_row][column],
                                                    matrix[second_row][column])
            matrix[row_to_apply].pop(column)
            matrix[row_to_apply].insert(column, adj_element)
            column += 1
        return matrix

    def matrix_mult_div_element(self, matrix, row, column, operator,
                                row_to_mult):
        """
        this function multiplies or divides rows of a given matrix and applies
        the operation to one of the two rows

        this will make a lot more sense if you are familiar

        :param matrix: the list of lists that needs to be multiplied or
               divided
        :param row: the row of the element that needs to be operated on
        :param column: the column of the element that needs to be operated on
        :param operator: a string that signifies what operation needs to be
               done
        :param row_to_mult: the row that the operation needs to be applied to
        :return: the adjusted matrix with the desired operations preformed
        """
        # this function multiplies entire rows of a matrix by a specific
        # element
        specified_element = matrix[row][column]
        num = 0
        if specified_element == 0:
            # to avoid division by zero error
            pass

        else:
            if operator == '*':
                while num < len(matrix[row]):
                    # You have to multiply the specified element with the
                    # opposite sign to the row that was already set to one
                    adj_element = self.operations[operator](
                        matrix[row_to_mult][num],
                        (specified_element * -1))
                    # W3 schools helped me find the pop() and insert()
                    # functions gets rid of the old element in the list
                    matrix[row_to_mult].pop(num)
                    # replaces the new element in its place
                    matrix[row_to_mult].insert(num, adj_element)

                    # adds one to move the index to pop and insert up by one
                    num += 1

                # you then add the row you just multiplied to the row with
                # the specified element
                self.matrix_add_sub(matrix, row, '+', row_to_mult, row)
                # set the row you multiplied back to its original state per
                # the rules of Gaussian elimination
                self.matrix_mult_div_element(matrix, row_to_mult, row_to_mult,
                                             '/', row_to_mult)

            else:
                while num < len(matrix[row]):
                    # please see the stack overflow article in the init
                    # dividing the specified element to the entire row that
                    # needs to be set to have a one in the right place
                    adj_element = self.operations[operator](matrix[row][num],
                                                            specified_element)
                    # W3 schools helped me find the pop() and insert()
                    # functions gets rid of the old element in the list
                    matrix[row].pop(num)
                    # replaces the new element in its place
                    matrix[row].insert(num, adj_element)

                    # adds one to move the index to pop and insert up by one
                    num += 1

            return matrix

    @staticmethod
    def usr_input(matrix, row, column):
        """
        this function gets user input and sets that input as the value at
        the proper index

        :param matrix: the list of lists that needs to be inputted in
        :param row: the amount of rows in the matrix
        :param column: the amount of columns in the matrix
        """
        print("Please enter your  matrix below.\nPlease just make "
              "sure that "
              "the first element on the first row is not a zero\n\n")

        # saves the input into the correct places in the matrix
        for i in range(row):
            for x in range(column):
                # if they enter anything that will not convert to a string
                # it will trigger a ValueError and is then handled
                try:
                    matrix[i][x] = float(input(
                        f'Please enter the [{i + 1}] [{x + 1}]'
                        ' element on the first row\n'))
                except ValueError:
                    print(
                        "type in a whole number or a reduced rational number"
                    )
                    try:
                        print("If you do not the program will input a zero "
                              "in this elements place")
                        matrix[i][x] = float(input(
                            f'Please enter element [{i + 1}] [{x + 1}]\n'))
                    except ValueError:
                        print("you have entered a invalid input too many "
                              "times, the program will input a 0")

    @staticmethod
    def f_output(num_rows, num_columns, matrix):
        """
        this function formats the output to be more pleasing to look at and
        logical

        :param num_rows: the amount of rows
        :param num_columns: the amount of columns
        :param matrix: the list of lists that needs its output formatted
        """
        for row in range(num_rows):
            for column in range(num_columns):
                # this program sometimes gives -0.0 for logical reasons its
                # set to 0
                if matrix[row][column] == -0.0:
                    matrix[row][column] = 0

                # this program goes into to high of precision and is now
                # limited to four places
                elif len(str(matrix[row][column]).replace(".", "")) > 5:
                    output = "{0:.4f}".format(matrix[row][column])
                    matrix[row][column] = output

        print("", matrix[0], "\n", matrix[1], "\n",
              matrix[2], "\n")


class GaussianElimination:
    """
class preforms the step by step process of Gaussian Elimination which you can
read about the here https://en.wikipedia.org/wiki/Gaussian_elimination
    """

    def __init__(self):
        self.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def reducer(self):
        """
        a function that oversees the step by step process of Gaussian
        Elimination

        first is setting the specified to one. Second is setting the rest of
        the elements in that column to zero
        """
        row_op = CommonMatrixOperations()
        row_op.usr_input(self.matrix, 3, 4)
        # to test if the last two rows were already switched

        # sets the first thee elements down to Reduced Row Echelon for
        # leaving the forth column as the answer
        row_op.matrix_mult_div_element(self.matrix, 0, 0, "/", 0)
        row_op.matrix_mult_div_element(self.matrix, 1, 0, "*", 0)
        row_op.matrix_mult_div_element(self.matrix, 2, 0, "*", 0)

        row_op.matrix_mult_div_element(self.matrix, 1, 1, "/", 1)
        row_op.matrix_mult_div_element(self.matrix, 0, 1, "*", 1)
        row_op.matrix_mult_div_element(self.matrix, 2, 1, "*", 1)

        row_op.matrix_mult_div_element(self.matrix, 2, 2, "/", 2)
        row_op.matrix_mult_div_element(self.matrix, 0, 2, "*", 2)
        row_op.matrix_mult_div_element(self.matrix, 1, 2, "*", 2)

        print("\n\nYour resulting matrix:")

        row_op.f_output(3, 4, self.matrix)

        print("\nThis is as far as this program can take your matrix as you"
              " have inputted it. If it is not fully reduced consider "
              "swapping the last two row.\n or making sure that the element ["
              "1][1] is not a zero")


class InverseMatrix:
    """
    this class finds the inverse of a a function using a similar method to
    Gaussian Elimination

    """

    def __init__(self):
        self.inverse_matrix = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 1]]

    def find_inverse(self):
        """
                a function that oversees the step by step process of finding
                the inverse matrix which is similar Gaussian Elimination

        first is setting the specified to one. Second is setting the rest of
        the elements in that column to zero

        all the elements on the left side of the identity matrix is the
        inverse of that matrix
        """
        # uses the methods from the CommonMatrix Operations class to find
        # the inverse of the matrix
        row_op = CommonMatrixOperations()
        # gets user input
        row_op.usr_input(self.inverse_matrix, 3, 3)
        try:
            # reduces the first three elements down to Reduced Row Echelon form
            # on one side with the identity on the other
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

            row_op.f_output(3, 6, self.inverse_matrix)
        except ZeroDivisionError:
            print("Your matrix has no inverse")

        print(
            'Please Remember that the inverse to your matrix is on the left '
            'side of the identity on the right if this matrix has an inverse')


def main():
    """
    the main function that oversees the operation and execution of the
    classes and functions of this program
    """
    print("Hello, welcome to my matrix calculator")
    choice = int(input(
        "For Gaussian Elimination(1), For finding the inverse of your "
        "matrix(2): "))
    print('\n')

    if choice == 1:
        GaussianElimination().reducer()
    if choice == 2:
        InverseMatrix().find_inverse()
    else:
        print("please select one of the options by entering the number along "
              "the side of the option \n")
        main()


main()
