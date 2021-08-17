import sys

import argparser
import hashlib

parser = argparser.parser()
parser.help_command("""
-h      Displays this command
--method        the method to hash with (sha512, sha256, sha384, sha224)
[flag] -capitalise      display the hash result with capitalisation
--text      text to hash (Doesn't support spaces, although this is going to be a future fix with my argparser)
""")
parser.add_argument("--method")
parser.add_argument('--text')
parser.add_flag("-capitalise")

hash_text = parser.get_argument("--text")
method = parser.get_argument("--method")

if method == "sha512":
    t = hashlib.sha512(hash_text.encode()).hexdigest()
    if parser.is_flag("-capitalise"):
        print(t.upper())
    else:
        print(t)
elif method == "sha256":
    t = hashlib.sha256(hash_text.encode()).hexdigest()
    if parser.is_flag("-capitalise"):
        print(t.upper())
    else:
        print(t)
elif method == "sha384":
    t = hashlib.sha384(hash_text.encode()).hexdigest()
    if parser.is_flag("-capitalise"):
        print(t.upper())
    else:
        print(t)
elif method == "sha224":
    t = hashlib.sha224(hash_text.encode()).hexdigest()
    if parser.is_flag("-capitalise"):
        print(t.upper())
    else:
        print(t)
else:
    print("Method not supplied or invalid method... use -h to see methods.\nExiting..")
    sys.exit()
