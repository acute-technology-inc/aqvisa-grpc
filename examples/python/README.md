# Sample Client in Python

This directory contains an example implementation for client in Python.

## Requirements

```
pip install -r requirements.txt
```

## Protobuf Complile

Please find `aqvisa.proto` in the `proto/` directory.

Execute the following command to compile

```
python -m grpc_tools.protoc -Iproto
                            --python_out=.
                            --pyi_out=.
                            --grpc_python_out=.
                            proto/aqvisa.proto
``````

For more information about protobuf, please visit [Protocol Buffers](https://protobuf.dev/) official website.

## Sample Codes

Please replace the `address` variable with your own ip and port first. You can obtain those values from the DSO or LA application.

### ViWrite & ViRead

Simply run the code to make a single request to the application

```
python write_read.py
```

Add any custom commands in `command_list` to try out any commands you prefer.

### ViWriteFromFile & ViReadToFile

Additionally replace the `json_file` variable with a dedicated path.

The, simply run the code to send a JSON payload to the application.

```
python write_file.py
```

Besides, you are able to request a JSON config from the application.

```
python read_file.py
```
