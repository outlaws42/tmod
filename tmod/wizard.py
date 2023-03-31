#! /usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Functions to work with doing a wizard to setup configuration files.
"""

# Standard Library Imports
from re import search

# Imports from tmods
from colors import (
    colors,
    prYellowBold,
    prGreen,
    prGreenBold,
)


__author__ = "Troy Franks"
__version__ = "2023-03-24"


# Input Functions


def input_list(
    subject: str,
    description: str,
    in_type: str = "email",
    outword: str = "next",
):
    """
    subject = The subject of the input item,
    description = the description of the input item,
    in_type = the type of input field. Choices are
    email, file, int, time, password
    outward = This is the word used to present to the user
    to stop adding more items.
    This would be used for a input item that you would
    want to add to a list.
    Requires: doesn't require any special imports
    """
    c = colors()
    print(
        f'\n{c["PURPLE"]}{c["BOLD"]}'
        f'{subject.capitalize()}{c["END"]}\n'
        f"You can add as many items as you like.\n"
        f"But you must add at least 1 item.\n"
        f"When your done adding, Type "
        f'{c["RED"]}{c["BOLD"]}{outword}{c["END"]}\n'
    )
    item_list = []
    while True:
        item: str = input(f"Enter the {subject} {description}: ")
        while validate_input(item, in_type) is False:
            if item.upper() == outword.upper() and len(item_list) != 0:
                break
            if item.upper() == outword.upper():
                print(
                    f'{c["RED"]}{c["BOLD"]}You need to enter at least 1 '
                    f'{in_type}{c["END"]}'
                )
            else:
                print(
                    f'{c["RED"]}{c["BOLD"]}This is not a valid ' f'{in_type}{c["END"]}'
                )
            item: str = input(f"Enter the {subject} {description}: ")
        if item.upper() == outword.upper() and len(item_list) != 0:
            length = len(item_list)
            print(
                f"\nYou have added {length} item(s), "
                f'Because you typed {c["RED"]}{c["BOLD"]}{item}{c["END"]}\n'
                f'That will complete your selection for "{subject.capitalize()}".'
            )
            break
        else:
            print(f'You added {c["CYAN"]}{item}{c["END"]}')
            item_list.append(item)
        print(f'{c["CYAN"]}{item_list}{c["END"]}')
    return item_list


def input_single(
    in_message: str,
    in_type: str = "email",
    fdest: str = "home",
    max_number: int = 200,
):
    """
    in_message = the message you want in your input string,
    in_type = the type of input field. Choices are
    email, file, int, time, password
    This is for a single item input. This uses "validate_input"
    to verify that items entered meet requirements for that type of input
    """
    c = colors()
    if in_type == "int" or in_type == "float":
        item = input(f"{in_message}(Max {max_number}): ")
    else:
        item = input(f"{in_message}: ")
    while (
        validate_input(
            item=item,
            in_type=in_type,
            fdest=fdest,
            max_number=max_number,
        )
        is False
    ):
        print(
            f'{c["RED"]}{c["BOLD"]}' f'This is not a valid {in_type}{c["END"]}',
        )
        if in_type == "int" or in_type == "float":
            item = input(f"{in_message}(max {max_number}): ")
        else:
            item = input(f"{in_message}: ")
    if in_type == "password":
        print(f'{c["CYAN"]}******{c["END"]}')
    else:
        print(f'You entered {c["CYAN"]}{item}{c["END"]}')
    if in_type == "int":
        return int(item)
    elif in_type == "float":
        return float(item)
    else:
        return item


def validate_input(
    item: str,
    in_type: str,
    fdest: str = "home",
    max_number: int = 200,
):
    """
    item = The data entered in the input field,
    email, file, password, int, float, time
    in_type = The type of data it is suposed to be,
    max_number = the max number that can be ablied this if for int only.
    Takes the input and checks to see if it is
    valid for its data type.
    """

    if in_type == "email":
        print(item)
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if search(regex, item):
            return True
        else:
            return False
    elif in_type == "file":
        if not item:
            return False
        else:
            return check_file_dir(item, fdest)
    elif in_type == "password":
        if not item:
            return False
    elif in_type == "time":
        try:
            datetime.strptime(item, "%H:%M").time()
            return True
        except ValueError:
            return False
    elif in_type == "int":
        try:
            number = int(item)
            if (number <= 0) or (number > max_number):
                return False
            return True
        except Exception:
            return False
    elif in_type == "float":
        try:
            number = float(item)
            if (number <= 0) or (number > max_number):
                return False
            return True
        except Exception:
            return False
    else:
        return False


# Wizard setup


def config_setup(conf_dir: str):
    """
    conf_dir = Configuration dir. This would
    normally be in the .config/progName,
    This commandline wizard creates the
    program config dir and populates the
    setup configuration file. Sets up username
    and password for email notifications
    """
    c = colors()
    home = home_dir()
    make_dir(conf_dir)

    print(
        f'\n{c["YELLOW"]}{c["BOLD"]}We could not find any '
        f'configuration folder{c["END"]}'
        f'\n{c["GREEN"]}This Wizard will ask some questions '
        f'to setup the configuration needed for the script to function.{c["END"]}'
        f'\n{c["GREEN"]}{c["BOLD"]}This configuration wizard will only run once.{c["END"]}\n'
        f'\n{c["GREEN"]}The first 2 questions are going '
        f"to be about your email and password you are using to send. "
        f"\nThis login information will be stored on your local "
        f"computer encrypted seperate "
        f"\nfrom the rest of the configuration. "
        f'This is not viewable by browsing the filesystem{c["END"]}'
    )

    gen_key(f"{conf_dir}/.info.key")
    key = open_file(fname=f"{conf_dir}/.info.key", fdest="home", mode="rb")
    prYellowBold(no_config)
    prGreen(intr_desc1)
    prGreenBold(intr_desc2)
    prGreen(intr_desc3)

    email = input_single(in_message="\nEnter your email", in_type="email")
    pas = input_single(in_message="\nEnter your password", in_type="password")
    lo = {email: pas}
    save_yaml(fname=f"{conf_dir}/.cred.yaml", fdest="home", content=lo)
    encrypt(
        key=key,
        fname=f"{conf_dir}/.cred.yaml",
        e_fname=f"{conf_dir}/.cred_en.yaml",
        fdest="home",
    )
    remove_file(f"{conf_dir}/.cred.yaml")
    run = input_single(
        in_message="Enter the time to run the script daily(Example: 05:00)",
        in_type="time",
    )
    numb_lines = input_single(
        in_message="Enter the number of lines from the end of log file to send",
        in_type="int",
        max_number=400,
    )
    send_list = input_list(
        subject="email address",
        description="to send to (example@gmail.com)",
        in_type="email",
    )
    log_list = input_list(
        subject="log file",
        description="to check relative to your home dir (Example: Logs/net_backup.log)",
        in_type="file",
    )
    load = {
        "runtime": run,
        "lines": int(numb_lines),
        "sendto": send_list,
        "logs": log_list,
    }
    save_yaml(fname=f"{conf_dir}/emailog_set.yaml", fdest="home", content=load)
    print(
        f'\n{c["YELLOW"]}{c["BOLD"]}This completes the wizard{c["END"]}'
        f"\nThe configuration file has been written to disk"
        f"\nIf you want to change the settings you can edit "
        f'{c["CYAN"]}{c["BOLD"]}{home}/{conf_dir}/emailog_set.yaml{c["END"]}'
        f'\n{c["GREEN"]}{c["BOLD"]}This wizard '
        f"won't run any more, So the script can "
        f'now be run automatically{c["END"]}\n'
        f'\n{c["CYAN"]}{c["BOLD"]}You can stop '
        f'the script by typing Ctrl + C{c["END"]}\n'
    )
