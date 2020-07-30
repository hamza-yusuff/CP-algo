def anagram(word1,word2):
    string1=''.join(sorted(word1))
    string2=''.join(sorted(word2))
    if string1==string2:
        print('anagram')
    else:
        print('NOT ANA')
anagram('cbb','bcb')
