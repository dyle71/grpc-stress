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

from google.protobuf import empty_pb2
import grpc

import server_pb2_grpc


def main():
    """Run the client."""

    channel = grpc.insecure_channel("127.0.0.1:5555")
    stub = server_pb2_grpc.ServerStub(channel)

    text = stub.get_text(empty_pb2.Empty(), timeout=5)
    sys.stdout.write(f"{text.timestamp:8.3f} - {text.text}\n")


if __name__ == '__main__':
    main()
