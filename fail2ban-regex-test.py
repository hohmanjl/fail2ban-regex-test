#!/usr/bin/python
"""
Tests fail2ban regex rules against a file and returns potential matches.
"""
import re
import sys
import argparse

__author__ = "James Hohman"
__license__ = "GPL"


def filter_file_gen(filter_file_):
    with open(filter_file_, 'r') as filter_file:
        fail_regex_found = False
        for line in filter_file:
            if line.startswith('failregex'):
                fail_regex_found = True
                line = line.split('=', 1)[-1]

            if fail_regex_found:
                line = line.strip()
                if not line:
                    fail_regex_found = False
                else:
                    yield line


def log_file_gen(log_file_):
    with open(log_file_, 'r') as log_file:
        for line in log_file:
            yield line


def search_log_file(log_files, regex):
    for log_file in log_files:
        sys.stdout.write("\n\n-- %s\n" % log_file)
        for line in log_file_gen(log_file):
            line = line.strip()
            re_search = re.search(regex, line)
            if re_search:
                sys.stdout.write(line + "\n")
                sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description='fail2ban regex match.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-f', '--filter-file', metavar='f', type=str, nargs='+',
        help='the fail2ban filter conf file'
    )
    group.add_argument(
        '-r', '--regex', metavar='r', type=str, nargs='+',
        help='a regex string to test'
    )

    parser.add_argument(
        '-l', '--log-file', required=True, metavar='l', type=str, nargs='+',
        help='the log file to search'
    )
    args = parser.parse_args()

    if args.filter_file is not None:
        for filter_file in args.filter_file:
            sys.stdout.write("\n%s" % filter_file)
            sys.stdout.flush()
            for regex in filter_file_gen(filter_file):
                sys.stdout.write("\n\n-- %s\n\n" % regex)
                sys.stdout.flush()

                regex = regex.replace("<HOST>", ".*")

                search_log_file(args.log_file, regex)

    if args.regex is not None:
        for regex in args.regex:
            sys.stdout.write("\n%s\n" % regex)
            regex = regex.replace("<HOST>", ".*")

            search_log_file(args.log_file, regex)


if __name__ == '__main__':
    main()
