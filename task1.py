def no_character(Statement):
    total_character = len(Statement)
    return total_character

def duplicate_character(Statement):
    total_character = len(Statement)
    original_char = set(Statement)
    dup_char = total_character - len(original_char)
    return dup_char

def no_words(Statement):
    words = Statement.split()
    total_words = len(words)
    return total_words

def duplicate_word_character(Statement):
    words = Statement.split()
    original_words = set(words)
    dup_word_count = len(words) - len(original_words)
    return dup_word_count

def reverse_char(Statement):
    rev_char = Statement[::-1]
    return rev_char

def reverse_word_new_statement(Statement):
    words = Statement.split()
    rev_word = ' '.join(reversed(words))
    new_statement = rev_word
    output = ' '
    for ch in new_statement:
        if ch not in output:
            output = output + ch
    
    return {
        "Reversed words": rev_word,
        "New statement from reversed words": new_statement,
        "Final statement without duplicate characters": output
    }


def Sentence():
    Statement=input("Enter the String: ")

    count_char = no_character(Statement)
    print("TOTAL NUMBER OF CHARACTERS IN A STATEMENT:", count_char)

    dupli_char = duplicate_character(Statement)
    print("TOTAL NUMBER OF DUPLICATE CHARACTERS IN A STATEMENT:", dupli_char)

    dupli_word = duplicate_word_character(Statement)
    print('TOTAL NUMBER OF DUPLICATE WORDS IN A STATEMENT:', dupli_word)

    reverse = reverse_char(Statement)
    print("REVERSING THE CHARACTERS PRESENT IN A STATEMENT:", reverse)

    result = reverse_word_new_statement(Statement)
    
    for key, value in result.items():
        print(key + ":", value)
    

Sentence()

