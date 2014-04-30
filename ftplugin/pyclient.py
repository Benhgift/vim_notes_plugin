from lib import argparse as argy
from os import system


def get_args():
    description = ("Interfaces with the running note server")
    parser = argy.ArgumentParser(description=description)
    parser.add_argument('-S', '--server', action='store_true', help='Starts notetool as a server and returns port')

    args = parser.parse_args()
    return args


def do_args(args):
    if args.server:
        return system('python ../note_study_tool/main.py -S')


if __name__ == '__main__':
    args = get_args()
    do_args(args)
