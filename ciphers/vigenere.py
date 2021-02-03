from .classical_cipher import ClassicalCipher
from string import ascii_uppercase


class Vigenere(ClassicalCipher):
    def __init__(self, original, key, mode):
        super().__init__(original, key)
        self.mode = mode                    # True: auto, False: repeating

    def encrypt(self):
        encrypted = ''
        key = ''
        if self.mode:
            key = self.key.upper() + self.plain
        else:
            for _ in range(int(len(self.plain) / len(self.key)) + 1):
                key += self.key.upper()

        for index, char in enumerate(self.plain):
            encrypted += ascii_uppercase[(ascii_uppercase.index(char) + ascii_uppercase.index(key[index])) % 26]

        return encrypted
