<h1 align=center>AqVISA with gRPC</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Acute VISA (simplified as AqVISA) offers an intuitive interface for seamless management of controlling our applications. With
 [gRPC](https://grpc.io/docs/), it makes even easier for developers to manipulate the automation workflow.

- **Acute official website**: https://www.acute.com.tw/en/
- **Acute software download**: https://www.acute.com.tw/en/install
- **AqVISA SDK download**: https://www.acute.com.tw/en/sdkDLL
- **Documentation**: https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/proto/README.md
- **Bug reports**: https://github.com/acute-technology-inc/aqvisa-grpc/issues

## Contents

[`examples/`](https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/examples/python)
contains sample client-side controlling flow code.

[`proto/`](https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/proto)
contains protocol buffer definition files.


## Supported Products

Products that support [gRPC](https://grpc.io/docs/) remote control

| Types                        | Product                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Mixed Signal Oscilloscope    | Acute MSO3000 series<br>Acute MSO2000 series<br>Acute MSO1000 series                                       |
| Digital Storage Oscilloscope | Acute TravelScope3000 series                                                                               |
| Logic Analyzer               | Acute TravelBus 3000 series<br>Acute TravelBus 2000 series<br>Acute TravelBus 1000 series<br>Acute TravelLogic 4000 series<br>Acute TravelLogic 3000 series<br>Acute LA4000 series<br>Acute LA3000 series |
| Protocol Analyzer            | Acute BusFinder 7000 series                                                                                |


## Minimium Requirements

Each product with its corresponding supported software version and platform is listed below. However, some features will require the application
with a newer version. Please check the [Releases](https://github.com/acute-technology-inc/aqvisa-grpc/releases/latest) page for details for each version.

### Windows

| Software (x64)                | Minimum Version | Download Link                               |
| ----------------------------- | --------------- | ------------------------------------------- |
| MSO                           | 1.8.10 or above | [Link](https://www.acute.com.tw/en/install) |
| MSO (Full)                    | 1.8.10 or above | [Link](https://www.acute.com.tw/en/install) |
| BusFinder and Logic Analyzer  | 1.8.09 or above | [Link](https://www.acute.com.tw/en/install) |
| TravelLogic                   | 1.8.05 or above | [Link](https://www.acute.com.tw/en/install) |
| TravelBus                     | 1.8.07 or above | [Link](https://www.acute.com.tw/en/install) |

### Linux

**_NOTE:_** The application on Linux platform are still marked as beta versions. Please create an issue if you encounter any errors when running the program.

| Software (x86_64)             | Minimum Version | Download Link                                                        |
| ----------------------------- | --------------- | -------------------------------------------------------------------- |
| Mixed_Signal_Oscilloscope     | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/mso-release/releases) |
| Digital_Storage_Oscilloscope  | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/dso-release/releases) |
| BusFinder_Logic_Analyzer      | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/bfa-release/releases) |
| TravelLogic_Analyzer          | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/tl-release/releases)  |
| TravelBus_Analyzer            | 2.0.0 or above  | [Link](https://github.com/acute-technology-inc/tba-release/releases) |

## References

- [gRPC documentation](https://grpc.io/docs/)
- [Protocol Buffers documentation](https://protobuf.dev/)
- [JSON schema](https://json-schema.org/draft/2020-12/release-notes)
