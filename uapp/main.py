#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from uapp.lib.args import handle_argument, handle_arguments, helper


def main():
    if len(sys.argv) <= 1:
        helper()

    if len(sys.argv) == 2:
        handle_argument(arg=sys.argv[1])
    if len(sys.argv) == 3:
        handle_arguments(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
