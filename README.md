# gRPC Stress

I run into some wired gRPC python client behavior: the client hangs on a call
though a timeout has been set.

Yet also the gRPC python server feels fine and has no problem at all... o.O 

This project helps investigating...


## Setup the virtual environment

```bash
$ python -m venv venv
$ source venv/bin/activate
```


## Create the protobuf files

Create the protobuf python files: 
```bash
$ source venv/bin/activate
$ python -m grpc_tools.protoc --proto_path=src/ --python_out=src/ --grpc_python_out=src/ src/server.proto 
```


## Run the single sample

A single run is
1. Start the server:
    ```bash
    $ source venv/bin/activate
    $ src/server.py
    ```

2. Start any number of clients:
    ```bash
    $ source venv/bin/activate
    $ src/client.py
    ```

Run those files with `--help` to see the additional options.

```bash
$ src/server.py --help
Usage: server.py [OPTIONS]

  Run the server.

Options:
  -a, --address TEXT           Address (IP:PORT) of server.  [default:
                               127.0.0.1:5555]
  --max-thread-worker INTEGER  Number of thread workers for gRPC.  [default:
                               10]
  -v, --verbose                Show the server text.
  -h, --help                   Show this message and exit.
```

```bash
$ src/client.py --help
Usage: client.py [OPTIONS]

  Run the client.

Options:
  -a, --address TEXT     Address (IP:PORT) of server.  [default:
                         127.0.0.1:5555]
  -n, --number INTEGER   Number of calls.  [default: 1000]
  -t, --timeout INTEGER  Timeout of gRPC call in seconds.  [default: 5]
  -v, --verbose          Show the server text.
  -h, --help             Show this message and exit.
```


## Let there be hell!

```bash
$ source venv/bin/activate
$ src/stress.py 
```



## Notable guidelines

* How (not) to write git commit messages: https://www.codelord.net/2015/03/16/bad-commit-messages-hall-of-shame/
* How to version your software: https://semver.org/
* How to write a clever "Changes" file: https://keepachangelog.com/en/1.0.0/
* Folder Convention: https://github.com/KriaSoft/Folder-Structure-Conventions


---

Copyright (C) 2022 headcode.space e.U.  
Oliver Maurhart <info@headcode.space>  
[https://headcode.space](https://www.headcode.space)
