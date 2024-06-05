# AqVISA with gRPC

This repository contains the gRPC .proto definition file that expose AqVISA APIs via gRPC, and a sample client code in Python.

## Supported Products

Products that support gRPC remote control

| Types                        | Product                                                                                                    | 
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Mixed Signal Oscilloscope    | Acute MSO3000 series<br>Acute MSO2000 series<br>Acute MSO1000 series                                       |
| Digital Storage Oscilloscope | Acute TravelScope3000 series                                                                               |
| Logic Analyzer               | Acute TravelBus 3000 series<br>Acute TravelBus 2000 series<br>Acute TravelBus 1000 series<br>Acute TravelLogic 4000 series<br>Acute TravelLogic 3000 series<br>Acute LA4000 series<br>Acute LA3000 series |
| Protocol Analyzer            | Acute BusFinder 7000 series                                                                                | 

Each product with its corresponding supported software version is listed below. 

## Platforms

### Windows

| Software (x64)                | Version         | Download Link                               |
| ----------------------------- | --------------- | ------------------------------------------- |
| MSO                           | 1.8.10 or above | [Link](https://www.acute.com.tw/en/install) |
| MSO (Full)                    | 1.8.10 or above | [Link](https://www.acute.com.tw/en/install) |
| BusFinder and Logic Analyzer  | 1.8.09 or above | [Link](https://www.acute.com.tw/en/install) |
| TravelLogic                   | 1.8.05 or above | [Link](https://www.acute.com.tw/en/install) |
| TravelBus                     | 1.8.07 or above | [Link](https://www.acute.com.tw/en/install) |

### Linux

**_NOTE:_** The software on Linux platform are still marked as beta versions. Please create an issue if you encounter any errors when running the program.

| Software (x86_64)             | Version         | Download Link                                                        |
| ----------------------------- | --------------- | -------------------------------------------------------------------- |
| Mixed_Signal_Oscilloscope     | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/mso-release/releases) |
| Digital_Storage_Oscilloscope  | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/dso-release/releases) |
| BusFinder_Logic_Analyzer      | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/bfa-release/releases) |
| TravelLogic_Analyzer          | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/tl-release/releases)  |
| TravelBus_Analyzer            | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/tba-release/releases) |

## Contents

`examples/` contains sample client-side code.

`proto/` contains protocol buffer definition files.

## References

* [Acute Official Website](https://www.acute.com.tw/en/)

* [Acute Software Download](https://www.acute.com.tw/en/install)

* [AqVISA docs](https://www.acute.com.tw/en/sdkDLL)

* [gRPC docs](https://grpc.io/docs/)

* [Protocol Buffer](https://protobuf.dev/)
