# XKCDPASS

Generate a "xkcd-style" random password.
Passwords contain an adjective, noun, verb, adverb, to have a change to construct a sentence. At least it might 
be pronouncable and memorizable, while still being quite safe. (there are 
[discussions](https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html) about this, but it still is better
than 'welcome123')

See https://xkcd.com/936/ for how this started originally

## Usage

    $ xkcdpass
    yielding-fishhook-dissolve-stormily
    

Limit (or extend) word length:

    $ xkcdpass --wordlength 4
    deft-roan-cork-ever
    
    $ xkcdpass --wordlength 10
    assumptive-gerrididae-sensualize-constantly

Limit total length:

    $ xkcdpass --maxlength 15
    gracious-anecdo
    
Use random-length words (more secure since we have more words in the list to choose from):

    $ xkcdpass --randomwordlength
    mongol-bud-feel-elaborately
    
To facilitate implementing bash-competion, the script can list all its commandline-options:

    $ xkcdpass --completion
    -h --help --maxlength -m --wordlength -w --randomwordlength -r --completion -c

    
Help text:

    $ xkcdpass --help
    usage: xkcdpass [-h] [--maxlen MAXLEN] [--wordlength WORDLENGTH]
                    [--randomworklength]
    
    generate a "XKCD-style" random password (https://xkcd.com/936/)
    
    optional arguments:
      -h, --help            show this help message and exit
      --maxlen MAXLEN, -m MAXLEN
                            Maximum length of password (default None)
      --wordlength WORDLENGTH, -w WORDLENGTH
                            length of words (default 8)
      --randomworklength, -r
                            use random-length words (more secure)
      --completion, -c      show options for facilicating bash completion                              
                            
## Installation

- make sure Python 3 is available on your system
- put script and word files in the same directory somewhere (in a git clone)
- symlink python script from a directory in your path (e.g. `ln -s /home/reinoud/git/xkcdpass/xkcdpass.py /usr/bin/xkcdpass`)

## bash completion

to facilitate bash completion, link the file `xkcdpass.bash_completion` from the `bash_completion.d` directory on your 
computer. When you run Brew with bash completion installed this would be something like:

    ln -s /home/reinoud/git/xkcdpass/xkcdpass.bash_completion /usr/local/etc/bash_completion.d/xkcdpass