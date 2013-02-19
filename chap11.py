# Jackie Gushue

# 11.9
def has_duplicates(array):
    storage = dict()
    for element in array:
        if element in storage:
            return "List has duplicates."
        storage[element] = 1
    return "List has no duplicates."

array = [1,2,3]
message = has_duplicates(array)
print message


# 11.10
def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    rotated_word = ''
    for letter in word:
        rotated_word += rotate_letter(letter, n)
    return res

def word_dict():
    word_dict = dict()
    in_file = open('words.txt', 'rU')
    for line in in_infile:
        word = line.strip().lower()
        word_dict[word] = word
    return word_dict

def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print word, i, rotated

word_dict = word_dict()
for word in word_dict:
    rotate_pairs(word, word_dict)
