## Known problems
The delimiters doesn't support spaces, infact none of supporst spaces. I will do it later if i can be bothered.

## Usage
```py
import argparser

parser = argparser.parser()

parser.add_argument("--test") 
parser.add_flag("-4")
parser.add_delimiter("--d")

print(parser.get_argument("--test")) # Returns the --test This_Here

print(parser.is_flag("-4")) # will return true/false if the flag is supplied in CLI arguments

print(parser.get_delimiter_arguments("--d")) # Will return array of ['delimiter_1', 'delimiter_2', 'delimiter_3']. (A delimiter is '--d delimiter_1,delimiter_2,delimiter_3')
```
