class ClassicalCipher:
    def __init__(self, original, key):
        self.original = original
        self.plain = ''.join(original.split()).upper()
        self.key = key

    def encrypt(self):
        pass
