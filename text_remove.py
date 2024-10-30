def remove_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    no_numbers_content = ''.join([i for i in content if not i.isdigit()])

    with open(file_path, 'w') as file:
        file.write(no_numbers_content)

# Use this function with the path to your text file
remove_numbers_from_file('/Users/rankuluw/Downloads/heisig-data.txt')

#def remove_first_character(file_path):
#    with open(file_path, 'r') as file:
#        content = file.read()

    # Remove the first character
#    updated_content = content[1:]

#    with open(file_path, 'w') as file:
#        file.write(updated_content)

# Use this function with the path to your text file
#remove_first_character('/Users/rankuluw/Downloads/heisig-data.txt')

def remove_duplicate_words_new_line(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    words = content.split()
    seen_words = set()
    unique_words = []

    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)

    updated_content = '\n'.join(unique_words)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# Use this function with the path to your text file
remove_duplicate_words_new_line('/Users/rankuluw/Downloads/heisig-data.txt')

import re

def remove_letters_colons_commas_dashes(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove all letters, colons, commas, and dashes
    updated_content = re.sub(r'[a-zA-Z:,-]', '', content)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# Use this function with the path to your text file
remove_letters_colons_commas_dashes('/Users/rankuluw/Downloads/heisig-data.txt')

def add_new_line_before_colon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = []
    i = 0
    while i < len(content):
        if content[i] == ':' and i > 0:
            updated_content.append('\n')
            updated_content.append(content[i-1])
        else:
            updated_content.append(content[i])
        i += 1

    final_content = ''.join(updated_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(final_content)

# Use this function with the path to your text file
add_new_line_before_colon('/Users/rankuluw/Downloads/eod2.txt')
