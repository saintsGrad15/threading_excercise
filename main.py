import ConfigParser
from Heartbeat.Heartbeat import Heartbeat
import random

config = ConfigParser.RawConfigParser()
config.read("threading_exercise.cfg")


def main():
    max_threads = config.getint("heartbeat", "max_num_threads")
    threads = []
    next_idx = 0

    for i in range(max_threads):
        hb = Heartbeat(next_idx, (random.random() + .1) * 2)
        hb.start()
        threads.append(hb)
        next_idx += 1

    try:
        while True:
                pass
    except KeyboardInterrupt as e:
        for thread in threads:
            thread.stop()

if __name__ == "__main__":
    main()
