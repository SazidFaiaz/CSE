import sys


def stringAnagram(dictionary, query):
    # Step 1: Normalize dictionary words and count anagrams
    anagram_count = {}
    for word in dictionary:
        normalized_word = ''.join(sorted(word))
        if normalized_word in anagram_count:
            anagram_count[normalized_word] += 1
        else:
            anagram_count[normalized_word] = 1

    # Step 2: For each query word, find the count of its anagrams
    result = []
    for word in query:
        normalized_word = ''.join(sorted(word))
        if normalized_word in anagram_count:
            result.append(anagram_count[normalized_word])
        else:
            result.append(0)

    return result


if __name__ == '__main__':
    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    print('\n'.join(map(str, result)))
