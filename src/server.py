#!/usr/bin/env python3

# ------------------------------------------------------------
# server.py
#
# gRPC stress server
#
# This file is part of the gRPC stress test investigation.
#
# The 'LICENSE.txt' file in the project root holds the software license.
# Copyright (C) 2022 headcode.space e.U.
# Oliver Maurhart <info@headcode.space>, https://www.headcode.space
# ------------------------------------------------------------

"""This implements the gRPC stress service server."""

from concurrent.futures import ThreadPoolExecutor
import sys
import time

import grpc

import server_pb2
import server_pb2_grpc


class ServerServicer(server_pb2_grpc.ServerServicer):
    """This is the gRPC stree server endpoint."""

    def __init__(self) -> None:
        super().__init__()
        self._message_count = 0

    def get_text(self, empty, context):

        self._message_count += 1

        text = server_pb2.Text()
        text.timestamp = time.time()
        text.text = f"This is message No. {self._message_count}."

        sys.stdout.write(f">>> {text.text}\n")
        sys.stdout.flush()

        return text


def main():
    """Run the server."""

    grpc_server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_ServerServicer_to_server(ServerServicer(), grpc_server)
    grpc_server.add_insecure_port(address="127.0.0.1:5555")
    grpc_server.start()

    sys.stdout.write(f"Server started.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ...
    sys.stdout.write(f"\nTerminating.\n")

    grpc_server.stop(grace=1.0)


if __name__ == '__main__':
    main()
