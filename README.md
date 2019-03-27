# XKCDPASS

Generate a "xkcd-style" random password.
Passwords contain an adjective, noun, verb, adverb, to have a change to construct a sentence. At least it might 
be pronouncable and memorizable, while still being quite safe. (there are discussions about this)

See https://xkcd.com/936/ for how this started originally

## Usage

    $ xkcdpass
    yielding-fishhook-dissolve-stormily
    

Limit (or extend) word length:

    $ xkcdpass -w 4
    deft-roan-cork-ever
    
    $ xkcdpass -w 10
    assumptive-gerrididae-sensualize-constantly

Limit total length:

    $ xkcdpass -m 15
    gracious-anecdo
    
Help text:

    $ xkcdpass -h
    usage: xkcdpass [-h] [--maxlen MAXLEN] [--wordlength WORDLENGTH]
    
    generate a "XKCD-style" random password (https://xkcd.com/936/)
    
    optional arguments:
      -h, --help            show this help message and exit
      --maxlen MAXLEN, -m MAXLEN
                            Maximum length of password
      --wordlength WORDLENGTH, -w WORDLENGTH
                            length of words
                            
                            
## Installation

- make sure Python 3 is available on your system
- put script and word files in the same directory somewhere
- symlink python script from a directory in your path (e.g. `ln -s /home/reinoud/scripts/xkcd/xkcdpass.py /usr/bin/xkcdpass`)