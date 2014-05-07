from multiprocessing.connection import Listener
from multiprocessing.connection import Client
from multiprocessing.pool import Pool
from collections import namedtuple
from lib import argparse as argy
from os import system
import signal
import sys
from threading import Thread


def _exit(signal, frame):
    sys.exit()


class ReturnableThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return


def get_args():
    description = ("Interfaces with the running note server")
    parser = argy.ArgumentParser(description=description)
    parser.add_argument('-S', '--server', help='Starts notetool as a server and returns port')
    parser.add_argument('-K', '--kill_server', help='Ends notetool server')
    args = parser.parse_args()
    return args


def _start_listener(listener):
    print("waiting")
    conn = listener.accept()
    address = conn.recv()
    listener.close()
    return address


def do_args(args):
    if args.server:
        listener = Listener()
        async_server = ReturnableThread(target=_start_listener, args=(listener,))
        async_server.start()
        system('nohup python ../note_study_tool/main.py -S ' + str(listener.address) + ' ' + args.server + ' &')
        client_loc =  async_server.join()
        client = Client(client_loc)
        com = ('exit', 0)
        client.send(com)
        return client_loc
    if args.kill_server:


if __name__ == '__main__':
    signal.signal(signal.SIGINT, _exit)
    args = get_args()
    print(do_args(args))
