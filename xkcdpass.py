#!/usr/bin/env python3

# xkcdpass - generate passwords in 'XKCD style'

import argparse
import os
import random

DEFAULT_MAXLEN = None
DEFAULT_WORDLENGTH = 8
WORDSFILES = ['adjectives', 'nouns', 'verbs', 'adverbs']
UNACCEPTABLECHARS = [' ', '-', '_']


def parse_args() -> argparse.Namespace:
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
    linenumber = random.randint(1, int(len(lines)/2))
    try:
        while True:
            word = lines[linenumber].strip().lower()
            if acceptable(word, wordlength):
                return word
            linenumber += 1
    except IndexError:
        print("ERROR: cannot find suitable words with this length")
        exit(1)


def readwordsfile(path: str) -> list:
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"ERROR: could not find file {path}")
        exit(2)
    except Exception as e:
        print(f"ERROR while reading file {path}: {e}")
        exit(3)


def gen_xkcdpass() -> str:
    args = parse_args()
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    words = {}
    passphrase = []
    for wordtype in WORDSFILES:
        words[wordtype] = readwordsfile(f'{scriptdir}/words.{wordtype}')
        passphrase.append(pickword(words[wordtype], args.wordlength))
    return '-'.join(passphrase)[:args.maxlen]


if __name__ == '__main__':
    print(gen_xkcdpass())



