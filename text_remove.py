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


