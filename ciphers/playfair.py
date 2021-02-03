from .classical_cipher import ClassicalCipher
from string import ascii_uppercase


class Playfair(ClassicalCipher):
    def __init__(self, original, key):
        super().__init__(original, key)
        self.matrix = []

    def _generate_matrix(self):
        self.matrix = [['' for _ in range(5)] for _ in range(5)]
        key = ''.join(self.key.split()).upper().replace('J', 'I')
        letters = ascii_uppercase.replace('J', '')
        index = 0

        for char in key:
            if letters.__contains__(char):
                self.matrix[int(index / 5)][index % 5] = char
                letters = letters.replace(char, '')
                index += 1

        for char in letters:
            self.matrix[int(index / 5)][index % 5] = char
            index += 1

    def _prepare_plain(self):
        temp = self.plain.replace('J', 'I') + ' '
        plain = temp[0]
        index = 1

        while index < len(temp) - 1:
            if temp[index] == plain[-1]:
                plain += 'X' + temp[index]
                index += 1

            else:
                plain += temp[index] + temp[index + 1]
                index += 2

        plain = plain.replace(' ', '')
        if len(plain) % 2 == 1:
            plain += 'X'

        return plain

    def _get_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return row, col

    def encrypt(self):
        self._generate_matrix()
        plain = self._prepare_plain()
        encrypted = ''
        index = 0

        while index < len(plain):
            row1, col1 = self._get_position(plain[index])
            row2, col2 = self._get_position(plain[index + 1])
            if row1 == row2:
                encrypted += self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted += self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
            else:
                encrypted += self.matrix[row1][col2] + self.matrix[row2][col1]
            index += 2

        return encrypted
