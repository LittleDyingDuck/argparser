import sys

"""
todo: write function for add flag,
 add delimiter argument,
 get argument for delimiter by name,
 get argument by index (helper function) # Done
"""

class parser:
    def __init__(self):
        self.flags = []
        self.arguments = []
        self.delimiters = []


    @staticmethod
    def help_command(help_text): # -h, --help, etc..
        for i in sys.argv:
            if i == "-h" or i == "--help":
                print(help_text)
                exit()

    def add_flag(self, flag):
        self.flags.append(flag)

    def is_flag(self, flag):
        if flag in sys.argv:
            return True
        return False

    def add_delimiter(self, delimiter):
        self.delimiters.append(delimiter)

    def get_delimiter_arguments(self, delimiter):
        if delimiter not in self.delimiters:
            raise Exception("Argument not found.")
        r = ""
        c = 0
        for i in sys.argv:
            c += 1
            if i == delimiter:
                r = sys.argv[c].split(',')# Still makes no sense.
                return r
        return None

    def is_delimiter(self, delimiter):
        if delimiter in self.delimiters:
            return True
        return False

    def is_argument(self, arg):
        if arg in self.arguments:
            return True
        return False

    def add_argument(self, arg):
        self.arguments.append(arg)

    def _get_delim_arg_by_idx(self, idx):
        return sys.argv[idx + 1]

    def get_argument(self, arg):
        if arg not in self.arguments:
            raise Exception("Argument not found.")
        r = ""
        c = 0
        for i in sys.argv:
            c += 1
            if i == arg:
                r = sys.argv[c] # This makes no fucking sense to me but apparently it works so.
                return r
        return None


    def get_flags(self):
        """
        :return: list
        """
        return self.flags

    def get_delimiters(self):
        """
        :return: list
        """
        return self.delimiters

    def get_args(self):
        """
        :return: list
        """
        return self.arguments

    @staticmethod
    def get_all_arguments():
        return sys.argv
