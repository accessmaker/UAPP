#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from colorama import Fore


def check_for_py_update():
    outdated_packages_str = os.popen("pip list -o --format json").read()
    if outdated_packages_str is not None:
        return outdated_packages_str
    else:
        print(f"All packages are up to date [{Fore.GREEN}OK{Fore.RESET}]")


def format_string_output(command_output):
    outdated_packages_str = command_output.replace("{", '')
    outdated_packages_str = outdated_packages_str.replace("}", '')
    outdated_packages_str = outdated_packages_str.replace("[", '')
    outdated_packages_str = outdated_packages_str.replace("]", '')
    outdated_packages_str = outdated_packages_str.replace("\"", '')
    outdated_packages_str = outdated_packages_str.replace("name: ", '')
    outdated_packages_str = outdated_packages_str.replace(" latest_version: ", '')
    outdated_packages_str = outdated_packages_str.replace(" latest_filetype: wheel,", '')
    outdated_packages_str = outdated_packages_str.replace(" latest_filetype: wheel", '')
    outdated_packages_str = outdated_packages_str.replace(" latest_filetype: sdist,", '')
    outdated_packages_str = outdated_packages_str.replace(" latest_filetype: sdist", '')
    outdated_packages_str = outdated_packages_str.replace(" version: ", '')
    outdated_packages_str = outdated_packages_str.replace(" ", ';\n')
    outdated_packages_list = outdated_packages_str.split(',;\n')
    return outdated_packages_list


def check_choice(packages_outdated):
    print('\n')
    option = input("Do you want to update? (Y or n)$ ")
    if option is None:
        option = 'y'
    option = option.lower()
    if option == 'n':
        exit()
    print('\n')
    return update_all(packages_outdated)


def format_package_list(outdated_packages_list) -> list:
    print("-"*50)
    print(f"{Fore.YELLOW}Outdated Packages:{Fore.RESET}")
    print("-" * 50+'\n')
    list_packages_outdated = []
    for outdated_package_str in outdated_packages_list:
        outdated_package_str = outdated_package_str.replace(',', '=')
        if outdated_package_str.count('=') > 2:
            outdated_package_str = outdated_package_str[:-2]
        print(outdated_package_str)
        list_packages_outdated.append(outdated_package_str)
    return list_packages_outdated


def update_all(package_list):
    for update in package_list:
        update = update.split('=')
        os.system(f"pip install --upgrade {update[0]} 2>/dev/null")
