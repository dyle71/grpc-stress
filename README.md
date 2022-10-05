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

Within the virtual environment (see above): 
```bash
$ python -m grpc_tools.protoc --proto_path=src/ --python_out=src/ --grpc_python_out=src/ src/server.proto 
```


## Run the sample

***TBD***



## Notable guidelines

* How (not) to write git commit messages: https://www.codelord.net/2015/03/16/bad-commit-messages-hall-of-shame/
* How to version your software: https://semver.org/
* How to write a clever "Changes" file: https://keepachangelog.com/en/1.0.0/
* Folder Convention: https://github.com/KriaSoft/Folder-Structure-Conventions


---

Copyright (C) 2022 headcode.space e.U.  
Oliver Maurhart <info@headcode.space>  
[https://headcode.space](https://www.headcode.space)
