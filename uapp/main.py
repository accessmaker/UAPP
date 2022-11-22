#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uapp.lib.utils import check_for_py_update, format_string_output, format_package_list, check_choice


def main():
    command = check_for_py_update()
    outdated_packages_list = format_string_output(command_output=command)

    packages_outdated = format_package_list(outdated_packages_list=outdated_packages_list)
    check_choice(packages_outdated)


if __name__ == '__main__':
    main()
