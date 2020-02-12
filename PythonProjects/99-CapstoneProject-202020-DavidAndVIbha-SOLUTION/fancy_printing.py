COLOR_CODES = {'black': 20,
               'red': 31,
               'green': 32,
               'yellow': 33,
               'blue': 34,
               'magenta': 35,
               'cyan': 36,
               'white': 37
               }


def print_colored(*args, color='black', **kwargs):
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1)
    sys.stdout.write('\033[%sm%s\033[0m' % (COLOR_CODES[color], text))
    print(**kwargs)
