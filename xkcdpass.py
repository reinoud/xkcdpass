#!/usr/bin/env python3

# xkcdpass - generate passwords in 'XKCD style'

import argparse
import random

DEFAULT_NUMWORDS=4
DEFAULT_MAXLEN=None
DEFAULT_WORDSFILE= '/usr/share/dict/web2a'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numwords', '-n', help='number of words', type=int, default=DEFAULT_NUMWORDS)
    parser.add_argument('--maxlen', '-m', help='Maximum length of password', type=int, default=DEFAULT_MAXLEN)
    parser.add_argument('--dictionaryfile', '-d', help='dictionary file to use', default=DEFAULT_WORDSFILE)
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.dictionaryfile) as wordsfile:
        lines=wordsfile.readlines()
        xkcdpasswords = []
        for line in range(args.numwords):
            words = lines[random.randint(1, len(lines))].strip().lower().replace('-', ' ').split()
            xkcdpasswords += words

        xkcdpass = '-'.join(xkcdpasswords[0:args.numwords])
        xkcdpass = xkcdpass[:args.maxlen]
        print(xkcdpass[:-1])


if __name__ == '__main__':
    main()



