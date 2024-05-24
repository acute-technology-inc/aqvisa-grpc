# AqVISA with gRPC

This repository contains the gRPC .proto definition file that expose AqVISA APIs via gRPC, and a sample client code in Python.

## Requirements

Products that support gRPC remote control

| Types                        | Product                                                                                                    | 
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Mixed Signal Oscilloscope    | Acute MSO3000 series<br>Acute MSO2000 series                                                               |
| Digital Storage Oscilloscope | Acute TravelScope 3000 series                                                                              |
| Logic Analyzer               | Acute TravelBus 3000 series<br>Acute TravelBus 2000 series<br>Acute TravelBus 1000 series<br>Acute TravelLogic 4000 series<br>Acute TravelLogic 3000 series<br>Acute LA4000 series<br>Acute LA3000 series |
| Protocol Analyzer            | Acute BusFinder 7000 series                                                                                | 

Each product with its corresponding supported software version is listed below. 

| Software (x64)          | Version         | 
| ----------------------- | --------------- |
| MSO                     | 1.7.62 or above |
| MSO (Full)              | 1.7.62 or above |
| BusFinder               | 1.7.57 or above |
| Logic Analyzer          | 1.7.57 or above |
| TravelLogic             | 1.7.36 or above |
| TravelBus               | 1.7.18 or above | 


## Contents

`examples/` contains sample client-side code.

`proto/` contains protocol buffer definition files.

## References

* [Acute Official Website](https://www.acute.com.tw/en/)

* [Acute Software Download](https://www.acute.com.tw/en/install)

* [AqVISA docs](https://www.acute.com.tw/en/sdkDLL)

* [gRPC docs](https://grpc.io/docs/)

* [Protocol Buffer](https://protobuf.dev/)
