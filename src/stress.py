#!/usr/bin/env python3

# ------------------------------------------------------------
# stress.py
#
# Take the client and the server to the extreme.
#
# This file is part of the gRPC stress test investigation.
#
# The 'LICENSE.txt' file in the project root holds the software license.
# Copyright (C) 2022 headcode.space e.U.
# Oliver Maurhart <info@headcode.space>, https://www.headcode.space
# ------------------------------------------------------------

"""This implements the gRPC stress orchestration."""

import pathlib
import os
import os.path
import subprocess
import time

import click


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--address', '-a', type=str, default='127.0.0.1:5555', show_default=True,
              help='Address (IP:PORT) of server.')
@click.option('--verbose', '-v', is_flag=True, help='Show the server text.')
def main(address: str, verbose: bool):
    """Fire up a server, call them a number of times via the client and kill em.

    Lather, rinse, repeat.
    """

    local_folder = pathlib.Path(__file__).parent

    client_cmd = [os.path.join(str(local_folder), 'client.py'), '--address', address, '--verbose']
    server_cmd = [os.path.join(str(local_folder), 'server.py'), '--address', address, '--verbose']

    max_duration = 10.0

    while True:

        client_stdout = open('client.out', 'w')
        client_stderr = open('client.err', 'w')
        server_stdout = open('server.out', 'w')
        server_stderr = open('server.err', 'w')

        server = subprocess.Popen(server_cmd, stdout=server_stdout, stderr=server_stderr)
        client = subprocess.Popen(client_cmd, stdout=client_stdout, stderr=client_stderr)

        start_polling = time.time()
        while client.poll() is None:
            if (time.time() - start_polling) >= max_duration:
                raise RuntimeError('Maximum duration for client passed! We have a problem.')
            time.sleep(0.1)

        server.kill()


if __name__ == '__main__':
    main()
