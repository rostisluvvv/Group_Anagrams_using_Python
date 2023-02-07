from collections import defaultdict


def group_anagrams(words):
    df_dict = defaultdict(list)

    for word in words:
        sorted_word = ' '.join(sorted(word))
        df_dict[sorted_word].append(word)
    return df_dict.values()


words = ["tea", "eat", "bat", "ate", "arc", "car"]

print(group_anagrams(words))