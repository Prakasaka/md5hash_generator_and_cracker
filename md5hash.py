#!/usr/bin/env python3

import hashlib
import time
import os
import sys
import argparse

# Color codes for strings
def red(red): return f"\033[1;31m{red}\033[0m"
def green(green): return f"\033[1;32m{green}\033[0m"
def yellow(yellow): return f"\033[1;33m{yellow}\033[0m"
def bold(bold): return f"\033[1m{bold}\033[0m"

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-W", "--wordlist", help="path-to-wordlist... default wordlist set to - wordlist.txt")
parser.add_argument("-S", "--string", help="Any strings here which one wants to you generated in md5hash")
parser.add_argument("--salt", type=int, help="1 for normal md5hash & 2 for double md5hash [default is 1]")
parser.add_argument("-M", "--md5hash", help="your generated md5hash value here")
parser.add_argument("-V", "--verbose", action="store_true", help="for verbose mode")
args = parser.parse_args()

# Function for generating md5hash
def md5hash_generating():
    if args.salt == 2:
        generated = hashlib.md5(args.string.encode('latin-1')).hexdigest()
        generated = hashlib.md5(generated.encode('latin-1')).hexdigest()
        print(yellow(f"Your double generated md5hash - {generated}"))
    else:
        generated = hashlib.md5(args.string.encode('latin-1')).hexdigest()
        print(yellow(f"Your generated md5hash - {generated}"))

# Running md5hash generating function
if args.string:
    md5hash_generating()
    sys.exit()

# If user won't give md5hash... script will show usage It will stuck 5-6 seconds cuz of default large wordlist
if not args.md5hash:
    os.system(f"python3 {sys.argv[0]} -h")

# default wordlist for linux
default_wordlist = '/usr/share/wordlists/rockyou.txt'
if os.path.exists(default_wordlist):
    if not args.wordlist:
        wordlist = default_wordlist
else:
    wordlist = args.wordlist

start = time.time()
# Function for cracking md5hash
def crack():
    try:
        with open(wordlist, 'r', encoding='latin-1') as lst:
            for word_list in lst.read().splitlines():
                if hashlib.md5(word_list.encode('latin-1')).hexdigest() == args.md5hash:
                    print(green(f"[✓] Found - {word_list}"))
                    end = time.time()
                    print(bold(f"\nTotal time taken - {end-start:.2f}s "))
                    break
                if args.verbose:
                    print(red(f"[✕] Wrong - {word_list}"))
    except FileNotFoundError:
        print(red("✕ Give me valid wordlist file path ✕"))

crack()
