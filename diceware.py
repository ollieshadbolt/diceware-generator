from secrets import randbelow

with open('beale.wordlist.asc.txt') as beale_wordlist_asc_txt:
    wordlist = beale_wordlist_asc_txt.readlines()

wordlist = [_[6:-1] for _ in wordlist[2:-10]]

while True:
    input(' '.join(wordlist[randbelow(len(wordlist))] for _ in range(7)))
