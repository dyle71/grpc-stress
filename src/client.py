#!/usr/bin/env python3

# ------------------------------------------------------------
# client.py
#
# gRPC stress client
#
# This file is part of the gRPC stress test investigation.
#
# The 'LICENSE.txt' file in the project root holds the software license.
# Copyright (C) 2022 headcode.space e.U.
# Oliver Maurhart <info@headcode.space>, https://www.headcode.space
# ------------------------------------------------------------

"""This implements the gRPC stress client."""

import sys

import click
from google.protobuf import empty_pb2
import grpc

import server_pb2_grpc


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--address', '-a', type=str, default='127.0.0.1:5555', show_default=True,
              help='Address (IP:PORT) of server.')
@click.option('--number', '-n', type=int, default=1000, show_default=True, help='Number of calls.')
@click.option('--timeout', '-t', type=int, default=5, show_default=True, help='Timeout of gRPC call in seconds.')
@click.option('--verbose', '-v', is_flag=True, help='Show the server text.')
def main(address: str, number: int, timeout: int, verbose: bool):
    """Run the client."""

    for i in range(number):

        channel = grpc.insecure_channel(address)
        stub = server_pb2_grpc.ServerStub(channel)

        try:
            text = stub.get_text(empty_pb2.Empty(), timeout=timeout)
        except grpc.RpcError as ex:
            print(f"Exception caught while calling server: {ex!s}")
            sys.exit(1)

        if verbose:
            sys.stdout.write(f"{text.timestamp:8.3f} - {text.text}\n")


if __name__ == '__main__':
    main()
