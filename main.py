from ciphers.caesar import Caesar
from ciphers.hill import Hill
from ciphers.playfair import Playfair
from ciphers.vernam import Vernam
from ciphers.vigenere import Vigenere


def read_file(name):
    file = open(name, 'r')
    str_list = []
    for line in file.readlines():
        str_list.append(line.replace('\n', ''))
    file.close()
    return str_list


def write_file(name, string):
    file = open(name, 'w')
    file.write(string)
    file.close()


print('Encrypting files...')

plain_list = read_file('caesar_plain.txt')
output = ''
for key in [3, 6, 12]:
    output += 'Key = ' + str(key) + '\n'
    for plain in plain_list:
        caesar = Caesar(plain, key)
        output += caesar.encrypt() + '\n'
    output += '\n'
write_file('caesar_cipher.txt', output)


plain_list = read_file('playfair_plain.txt')
output = ''
for key in ['rats', 'archangel']:
    output += 'Key = ' + key + '\n'
    for plain in plain_list:
        playfair = Playfair(plain, key)
        output += playfair.encrypt() + '\n'
    output += '\n'
write_file('playfair_cipher.txt', output)


plain_list = read_file('hill_plain_2x2.txt')
output = ''
output += '      |5  17|\n'
output += 'Key = |     |\n'
output += '      |8   3|\n\n'
for plain in plain_list:
    hill = Hill(plain, [[5, 17], [8, 3]])
    output += hill.encrypt() + '\n'
write_file('hill_cipher_2x2.txt', output)


plain_list = read_file('hill_plain_3x3.txt')
output = ''
output += '      |2   4  12|\n'
output += 'Key = |9   1   6|\n'
output += '      |7   5   3|\n\n'
for plain in plain_list:
    hill = Hill(plain, [[2, 4, 12], [9, 1, 6], [7, 5, 3]])
    output += hill.encrypt() + '\n'
write_file('hill_cipher_3x3.txt', output)


plain_list = read_file('vigenere_plain.txt')
output = 'Key = pie\t(repeating mode)\n'
for plain in plain_list:
    vigenere = Vigenere(plain, 'pie', False)
    output += vigenere.encrypt() + '\n'

output += '\nKey = aether\t(auto mode)\n'
for plain in plain_list:
    vigenere = Vigenere(plain, 'aether', True)
    output += vigenere.encrypt() + '\n'
output += '\n'
write_file('vigenere_cipher.txt', output)


plain_list = read_file('vernam_plain.txt')
output = 'Key = SPARTANS\n'
for plain in plain_list:
    vernam = Vernam(plain, 'SPARTANS')
    output += vernam.encrypt() + '\n'
write_file('vernam_cipher.txt', output)

print('Files encrypted successfully.\n')


while 1:
    choice = input('Do you want to encrypt an alphabetical text? (Y-N): ')
    if choice == 'N' or choice == 'n':
        break
    elif choice == 'Y' or choice == 'y':
        plain = input('Enter your text: ')
        key_caesar = int(input('Caesar cipher key: '))
        key_playfair = input('Playfair cipher key: ')
        key_vernam = input('Vernam cipher key: ')
        key_vigenere = input('Vigenere cipher key: ')

        row = input('Hill cipher matrix row no. 1: ')
        row = (' '.join(row.split())).split()
        key_hill = [row]
        for i in range(len(row) - 1):
            row = input('Hill cipher matrix row no. ' + str(i + 2) + ': ')
            row = (' '.join(row.split())).split()
            key_hill.append(row)
        for row in range(len(key_hill)):
            for col in range(len(key_hill)):
                key_hill[row][col] = int(key_hill[row][col])

        print('\n')
        cipher = Caesar(plain, key_caesar)
        print('Caesar cipher: ' + cipher.encrypt())
        cipher = Playfair(plain, key_playfair)
        print('Playfair cipher: ' + cipher.encrypt())
        cipher = Vernam(plain, key_vernam)
        print('Vernam cipher: ' + cipher.encrypt())
        cipher = Vigenere(plain, key_vigenere, True)
        print('Vigenere cipher (auto mode): ' + cipher.encrypt())
        cipher = Vigenere(plain, key_vigenere, False)
        print('Vigenere cipher (repeating mode): ' + cipher.encrypt())
        cipher = Hill(plain, key_hill)
        print('Hill cipher: ' + cipher.encrypt())
        print('\n')
