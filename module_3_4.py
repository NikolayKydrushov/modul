def single_root_words(root_word, *other_words):
    same_words = []
    same_words2 = []
    root_word = root_word.lower()

    for i in range(len(other_words)):
        same_words2.append(other_words[i])

    for i in range(len(same_words2)):

        same_words2[i] = same_words2[i].lower()

        if root_word in same_words2[i] or same_words2[i] in root_word:
            same_words.append(other_words[i])

    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))