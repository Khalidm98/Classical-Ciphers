from .classical_cipher import ClassicalCipher
from string import ascii_uppercase
from numpy import dot


class Hill(ClassicalCipher):
    def encrypt(self):
        index = 0
        encrypted = ''
        plain = self.plain
        dimensions = len(self.key)
        for _ in range((dimensions - (len(plain) % dimensions)) % dimensions):
            plain += 'X'

        while index < len(plain):
            column = []
            for i in range(dimensions):
                column.append([ascii_uppercase.index(plain[index + i])])
            product = dot(self.key, column)
            for i in range(dimensions):
                encrypted += ascii_uppercase[product[i][0] % 26]
            index += dimensions

        return encrypted
