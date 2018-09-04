import signal
import logging
import time
import os
exit_flag = False

logging.basicConfig(filename='log.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other
    signals can be mapped here as well (SIGHUP?)
    Basically it just sets a global flag, and main()
    will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    logging.debug('Program has stopped.')
    logging.debug('Received ' + signal.Signals(sig_num).name)
    exit_flag = True


def main():
    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if
    # OS sends either of these to my process.

    if not exit_flag:
        logging.debug('Program has started.')

    dir = "directory"
    magic_text = "butts"

    while not exit_flag:
        # Do my long-running stuff
        for file in os.listdir(dir):
            text = open(dir + "/" + file).read().split('\n')
            for i, line in enumerate(text):
                if magic_text in line:
                    log = 'magic text in ' + file + ' in line ' + str(i)
                    if log not in open("log.log").read():
                        logging.info('magic text in ' + file +
                                     ' in line ' + str(i))

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(10)


if __name__ == '__main__':
    main()
