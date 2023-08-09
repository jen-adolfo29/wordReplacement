# word replacement
def replace_word():
    str = "A sentence or statement. It could be a phrase."
    word_to_replace = input("Word to replace: ")
    word_replacement = input("Word replacement: ")
    print(str.replace(word_to_replace, word_replacement))
replace_word()