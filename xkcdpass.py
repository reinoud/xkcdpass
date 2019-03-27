#!/usr/bin/env python3

# xkcdpass - generate passwords in 'XKCD style'

import argparse
import os
import random

DEFAULT_MAXLEN = None
DEFAULT_WORDLENGTH = 8
WORDSFILES = ['adjectives', 'nouns', 'verbs', 'adverbs']
UNACCEPTABLECHARS = [' ', '-', '_']


def parse_args():
    parser = argparse.ArgumentParser(description='generate a "XKCD-style" random password (https://xkcd.com/936/)')
    parser.add_argument('--maxlen', '-m', help='Maximum length of password', type=int, default=DEFAULT_MAXLEN)
    parser.add_argument('--wordlength', '-w', help='length of words', type=int, default=DEFAULT_WORDLENGTH)
    return parser.parse_args()


def acceptable(word: str, length: int = None) -> bool:
    if word is None or len(word) == 0:
        return False
    for char in UNACCEPTABLECHARS:
        if char in word:
            return False
    if length is not None and len(word) != length:
        return False
    return True


def pickword(lines: list, wordlength: int = None) -> str:
    linenumber = random.randint(1, len(lines))
    while True:
        word = lines[linenumber].strip().lower()
        if acceptable(word, wordlength):
            return word
        linenumber += 1


def readwordsfile(path: str) -> list:
    with open(path) as file:
        return file.readlines()


def main():
    args = parse_args()
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    words = {}
    passphrase = []
    for wordtype in WORDSFILES:
        words[wordtype] = readwordsfile(f'{scriptdir}/words.{wordtype}')
        passphrase.append(pickword(words[wordtype], args.wordlength))

    xkcdpass = '-'.join(passphrase)
    xkcdpass = xkcdpass[:args.maxlen]
    print(xkcdpass)


if __name__ == '__main__':
    main()



