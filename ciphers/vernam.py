from .classical_cipher import ClassicalCipher
from string import ascii_uppercase


class Vernam(ClassicalCipher):
    def encrypt(self):
        encrypted = ''
        key = ''.join(self.key.split()).upper()
        for index, char in enumerate(self.plain):
            encrypted += ascii_uppercase[(ascii_uppercase.index(char) + ascii_uppercase.index(key[index])) % 26]

        return encrypted
