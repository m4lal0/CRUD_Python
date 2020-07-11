# By @M4lal0
# -*- coding: utf-8 -*-

import sys,csv,os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print(bcolors.FAIL + "Client already is in the client´s list" + bcolors.ENDC)


def update_client(client_id, updated_client):
    global clients
    
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print(bcolors.FAIL + "Client is not in client´s list" + bcolors.ENDC)


def delete_client(client_id):
    global clients
    
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def list_clients():
    print("UID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION")
    print("*" * 60)
    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}". format(uid=idx, name=client['name'], company=client['company'], email=client['email'], position=client['position']))


def _get_client_field(field_name, message="What is the client {}? : "):
    field = None

    while not field:
        field = input(message.format(field_name))
    
    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    return client


def display_banner():
    banner ="\n ______  _______  __    __ _______  \n"
    banner +=" /      \|       \|  \  |  \       \ \n"
    banner +="|  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\ \n"
    banner +="| ▓▓   \▓▓ ▓▓__| ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓\n"
    banner +="| ▓▓     | ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓\n"
    banner +="| ▓▓   __| ▓▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓  | ▓▓\n"
    banner +="| ▓▓__/  \ ▓▓  | ▓▓ ▓▓__/ ▓▓ ▓▓__/ ▓▓\n"
    banner +=" \▓▓    ▓▓ ▓▓  | ▓▓\▓▓    ▓▓ ▓▓    ▓▓\n"
    banner +="  \▓▓▓▓▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓▓ \n"
    banner +="--[ Create | Read | Update | Delete ]--\n"
    banner +="--[             v20.01              ]--\n"
    return print(bcolors.HEADER + banner + bcolors.ENDC)


def display_menu():
    print("What would you like to do today?")
    print("[C]reate client")
    print("[R]ead client´s")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")
    print("[E]xit")


if __name__ == '__main__':
    _initialize_clients_from_storage()
    display_banner()
    display_menu()

    command = input(bcolors.BOLD + "Option: " + bcolors.ENDC)
    command = command.upper()

    if command == "C":
        client = _get_client_from_user()
        create_client(client)
    elif command == "R":
        list_clients()
    elif command == "U":
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == "D":
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == "S":
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print(bcolors.OKGREEN + "The client is in the client´s list" + bcolors.ENDC)
        else:
            print(bcolors.FAIL+ "The client: {0} is not in our client´s list".format(client_name) + bcolors.ENDC)
    elif command == "E":
        sys.exit()
    else:
        print(bcolors.FAIL + "Invalid command" + bcolors.ENDC)
    
    _save_clients_to_storage()