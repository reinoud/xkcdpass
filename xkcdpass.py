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
        raise Exception("xkcd pass ERROR: cannot find suitable words with this length")


def readwordsfile(path: str) -> list:
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"xkcd pass ERROR: could not find file {path}")
    except Exception as e:
        raise Exception(f"xkcd pass ERROR while reading file {path}: {e}")


def gen_xkcdpass() -> str:
    args = parse_args()
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    words = {}
    passphrase = []
    for wordtype in WORDSFILES:
        words[wordtype] = readwordsfile(f'{scriptdir}/xwords.{wordtype}')
        passphrase.append(pickword(words[wordtype], args.wordlength))
    return '-'.join(passphrase)[:args.maxlen]


if __name__ == '__main__':
    try:
        print(gen_xkcdpass())
    except Exception as e:
        print(e)
        exit(1)



