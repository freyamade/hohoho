import argparse
from .hohoho import boobooboo_to_whitespace
from .translator import whitespace_to_boobooboo

parser = argparse.ArgumentParser(description='BooBooBoo, the FESTIVE esolang! (powered by whitespace)', prog='hohoho')
parser.add_argument(
    'file',
    metavar='input_file',
    type=str,
    help='Input file. Should be a .ho file unless you\'re translating from whitespace to boobooboo',
)
parser.add_argument(
    '--from-ws',
    '-t',
    action='store_const',
    const=True,
    default=False,
    help='Translate an input whitespace file into a boobooboo file.',
)

def main():
    args = parser.parse_args()
    input_file = args.file
    translate = args.from_ws

    if translate:
        # Translate the .ws file to .ho
        out_name = input_file.split('.')[0] + '.ho'
        whitespace_to_hohoho(input_file, out_name)
    else:
        boobooboo_to_whitespace(input_file)

if __name__ == '__main__':
    main()
