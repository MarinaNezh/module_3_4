def single_root_words(root_word , *other_words):
    same_words = []
    for i in other_words:
        if root_word in i or i in root_word:
            same_words.append(i)
    return same_words
result = single_root_words('пол', 'половое', 'однополый', 'бесполый', 'плотный')
print(result)

