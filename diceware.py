from secrets import randbelow

with open('beale.wordlist.asc.txt') as beale_wordlist_asc_txt:
    wordlist = beale_wordlist_asc_txt.readlines()

wordlist = [word[6:-1] for word in wordlist[2:-10]]

while True:
    input(' '.join(wordlist[randbelow(len(wordlist))] for word in range(7)))
