# AqVISA with gRPC

This repository contains the gRPC .proto definition file that expose AqVISA APIs via gRPC, and a sample client code in Python.

## Requirements

Products that support gRPC remote control

* Mixed Signal Oscilloscope
    
    * Acute MSO3000 series
    * Acute MSO2000 series

* Digital Storage Oscilloscope

    * Acute TravelScope3000 series

Only support on software version from `1.7.62` or above.

## Contents

`examples` contains sample client-side code.

`proto` contains protocol buffer definition files.

## References

* [AqVISA docs](https://www.acute.com.tw/logic-analyzer-en/support/download/sdk-dll)

* [gRPC docs](https://grpc.io/docs/)

* [Protocol Buffer](https://protobuf.dev/)
