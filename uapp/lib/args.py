#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uapp import __Version__
from uapp.lib.utils import check_for_py_update, format_string_output, format_package_list, check_choice


def handle_argument(arg):
    if arg == 'check-update':
        command = check_for_py_update()
        outdated_packages_list = format_string_output(command_output=command)
        format_package_list(outdated_packages_list=outdated_packages_list)

    elif arg == 'update' or arg == 'upgrade':
        command = check_for_py_update()
        outdated_packages_list = format_string_output(command_output=command)
        packages_outdated = format_package_list(outdated_packages_list=outdated_packages_list)
        check_choice(packages_outdated)

    elif arg == 'version' or arg == '--version':
        print(f'uapp v:{__Version__}')
    elif arg == 'help' or arg == '--help' or arg == '-h':
        helper()
    else:
        helper()


def handle_arguments(arg1, arg2):
    if arg1 == 'update' or arg1 == 'upgrade':
        command = check_for_py_update()
        outdated_packages_list = format_string_output(command_output=command)
        packages_outdated = format_package_list(outdated_packages_list=outdated_packages_list, chosen_package=arg2)
        check_choice(packages_outdated=packages_outdated, arg_package=arg2)
    else:
        helper()


def helper():
    print('''
UAPP(Update All Python Packages):is an unofficial package manager, which makes it easy to update packages installed with pip
    OPTIONS:
        help, --help or -h = show uapp help options;
        version, --version = show uapp version;
        check-update = Search and show available updates;
        update, upgrade = Update all packages;
        update package = Update the selected package.
''')
