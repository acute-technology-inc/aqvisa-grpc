# Sample Client in Python 

This directory contains an example implementation for client in Python. 

## Requirements

pip install -r requirements.txt

## Protobuf Complile

Please find `aqvisa.proto` in the `proto/` directory.

Execute the following command to compile 

For more information about protobuf, please visit [Protocol Buffers](https://protobuf.dev/) official website.

```
python -m grpc_tools.protoc -Iproto 
                            --python_out=. 
                            --pyi_out=. 
                            --grpc_python_out=. 
                            proto/aqvisa.proto
``````

## Sample Client



Before excuting `client.py`, please replace the `address` variable with your own ip and port. You can obtain those values from the DSO / LA software. 

```
python client.py
```

Simply add any custom commands in `command_list` to try out any commands you prefer.