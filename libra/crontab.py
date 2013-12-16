#!/usr/bin/python
import os
import sys
import getopt
import logging


def usage():
    print("usage() not implemented")


def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hc", ["help", "collect"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    collect_flag = False

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", "--collect"):
            collect_flag = True

    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath("%s/.." % project_root))

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        filename="crontab.log",
        filemode='a'
    )

    if collect_flag:
        from libra.cron import collect
        collect.run()

if __name__ == "__main__":
    main()
