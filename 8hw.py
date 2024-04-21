def count_matches(word, symbol):

    word,symbol = input('Anna','a')

    count_match = 0
    count_not_match = 0
    for letter in word:
        if letter == symbol:
            count_match += 1
        else:
            count_not_match += 1
    return count_match, count_not_match

assert count_matches('Anna', 'a') == (2)