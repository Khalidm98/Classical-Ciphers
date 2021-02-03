from .classical_cipher import ClassicalCipher
from string import ascii_uppercase


class Caesar(ClassicalCipher):
    def encrypt(self):
        encrypted = ''
        for char in self.plain:
            encrypted += ascii_uppercase[(ascii_uppercase.index(char) + self.key) % 26]
        return encrypted
