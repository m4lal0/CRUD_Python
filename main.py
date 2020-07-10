# By @M4lal0
# -*- coding: utf-8 -*-

import sys,csv,os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def display_banner():
    print("What would you like to do today?")
    print("[C]reate client")
    print("[R]ead client\´s")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")
    print("[E]xit")


if __name__ == '__main__':
    _initialize_clients_from_storage()
    display_banner()

    command = input("Option: ")
    command = command.upper()

    if command == "C":
        pass
    elif command == "R":
        pass
    elif command == "U":
        pass
    elif command == "D":
        pass
    elif command == "S":
        pass
    elif command == "E":
        sys.exit()
    else:
        print("Invalid command")