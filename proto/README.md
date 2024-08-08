# AqVISA RPC Documentation

In the section, we will simply go through AqVISA flow and introduce all supported AqVISA RPCs.

## Flow Chart

<p align="center">
    <img src="https://github.com/acute-technology-inc/aqvisa-grpc/blob/main/res/flowchart.png?raw=true"/>
</p>

Simply send commands via [ViWrite](#ViWrite) call. The server will generate a response after the command is fully executed. If there is queried value to be returned, you can retrieve the value by using [ViRead](#ViRead) call. Repeat this flow for your automation process. For more details, please read the next section for all defined RPC calls.

## RPCs

### ViRead

Query response values if any from the previous requesting command sent by [ViWrite](#ViWrite).

See also [ViReadRequest](#ViReadRequest) and [ViReadResponse](#ViReadResponse) messages.

### ViWrite

Send commands to the application with the parameter *command*. Return AQVI_NO_ERROR when successfully executed. Otherwise, the server responses a error code defined in AQVI_STATUS.

See also [ViWriteRequest](#ViWriteRequest) and [ViWriteResponse](#ViWriteResponse) messages.

### ViWriteFromFile

This RPC is used for send configuration file instead of sending commands to the application. The configuration file is in *JSON* format. It is loaded and the payload can be transferred over gRPC.

See also [ViWriteFromFileRequest](#ViWriteFromFileRequest) and [ViWriteFromFileResponse](#ViWriteFromFileResponse) messages.

For the *JSON* config, please see [**schema**](https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/config/schemas) for more details.

## Messages

### ViReadRequest

* Parameter

    - bytes ***jobid*** [deprecated]: NOT IN USE.
    - int64 ***count***: Represents the size of the data buffer to receive data from the application.

### ViReadResponse

* Parameter

    - [AQVI_STATUS](#AQVI_STATUS) ***status_code***: Return status.
    - bytes ***command_response***: Queried response from the previous [ViWrite](#ViWrite) command.
    - int64 ***ret_count***: Represents the length of the responses

### ViWriteRequest

* Parameter

    - bytes ***command***: A byte array command that is ready to be sent to the application.

### ViWriteResponse

* Parameter

    - bytes ***jobid***: Represents the unique identification of the ViWrite call.
    - [AQVI_STATUS](#AQVI_STATUS) ***status_code***: Return status.

### ViWriteFromFileRequest

* Parameter

    - bytes ***payload***: A byte array payload loaded from JSON configuration file.
    Currently supported schema is as follows


        | Schema Name | Schema |
        | ----------- | ------ |
        | Electrical Validation | [Schema](../config/schemas/ev/ev.schema.json) |

### ViWriteFromFileResponse

* Parameter

    - bytes ***jobid***: Represents the unique identification of the [ViWriteFromFile](#ViWriteFromFile) call.
    - [AQVI_STATUS](#AQVI_STATUS) ***status_code***: Return status.

### ViReadToFileRequest

* Parameter

    - [AQVI_JSON_SCHEMA](#AQVI_JSON_SCHEMA) ***schema_type***: Logical index of schema type
    - int64 ***count***: Input buffer size for accepting requested payload
    Currently supported schema is as follows


        | Schema Name | Schema |
        | ----------- | ------ |
        | Electrical Validation | [Schema](../config/schemas/ev/ev.schema.json) |

### ViReadToFileResponse

* Parameter

    - [AQVI_STATUS](#AQVI_STATUS) ***status_code***: Return status.
    - bytes ***payload***: Requested JSON payload
    - int64 ***ret_count***: Requested JSON payload size

## Status Code

### AQVI_JSON_SCHEMA

| Value | Enum | Description |
| ----- | ---- | ----------- |
| **0** | AQVI_JSON_SCHEMA_DUMMY | Not in use |
| **1** | AQVI_JSON_SCHEMA_ELECTRICAL_VALIDATION | Electrical Validation Configuration|

### AQVI_STATUS

| Value | Enum | Description |
| ----- | ---- | ----------- |
| **0** | AQVI_NO_ERROR | No Error |
| **2** | AQVI_APPLICATION_NOT_STARTED | Error: The main software application was not started|
| **7** | AQVI_NO_RETURN_DATA | Warn: There's no any data returned. |
| **9** | AQVI_DATA_BUFFER_TOO_SMALL | Warn: Input data buffer size is too small |
| **12** | AQVI_PREVIOUS_CMD_PROCESSING | Warn: Previous command still processing |
| **13** | AQVI_INPUT_PARAMETER_UNKNOWN | Error: Input parameter unknown or not supported |
| **14** | AQVI_INPUT_PARAMETER_INCOMPLETED | Error: Input parameter incompleted |
| **15** | AQVI_TIMEOUT | Error: Input request timeout |
| **1000** | AQVI_NOT_SUPPORTED | Error: Not supported in current software |
| **1001** | AQVI_INCOMPLETE_COMMAND | Error: Command incomplete |
| **1002** | AQVI_SUBWND_INVALID | Error: Input command requires exist SubWindow |
| **1003** | AQVI_SUBWND_CNT_EXCEED | Error: Exceed maximum page count as requested |
| **1004** | AQVI_SW_BUSY | Error: Input command ignored while software busy |
| **1005** | AQVI_LASUBWND_INVALID | Error: Input command requires exist Logic Analyzer SubWindow |
| **1006** | AQVI_PASUBWND_INVALID | Error: Input command requires exist Protocol Analyzer SubWindow |
| **1007** | AQVI_DECODE_REPORT_INVALID | Error: Input command requires existing Decode Report |
| **1008** | AQVI_TIMING_REPORT_INVALID | Error: Input commands requires exist Timing Report |
| **1009** | AQVI_COMMAND_FORMAT_ERROR | Error: Command formate error |
| **1010** | AQVI_INPUT_FILE_DIR_INVALID | Error: Incorrect input file |
| **1011** | AQVI_CAPTURE_ALREADY_RUNNING | Error: Sending Capture Start command while capture already running |
| **1012** | AQVI_CAPTURE_NOT_RUNNING | Error: Sending Capture Stop command while capture is not running |
| **1013** | AQVI_ROW_COL_INDEX_INVALID | Error: Input Row or Column index invalid |
| **1014** | AQVI_SELECT_INDEX_INVALID | Error: Input index selection invalid |
| **1015** | AQVI_INPUT_PARAMETER_INVALID | Error: Missing input parametes or not enough input parameter |
| **1016** | AQVI_INPUT_SETTING_FILE_FORMAT_ERROR | Error: Input settings file format error |
| **1017** | AQVI_FILE_ACCESS_ERROR | Error: Unable to reach select file directory |
| **1018** | AQVI_TRANSITION_REPORT_INVALID |  Error: Input commands requires exist Transition Report |
| **1019** | AQVI_MEASUREMENT_REPORT_INVALID | Error: Input commands requires existint measurement report |
| **1020** | AQVI_SELECT_LABEL_INVALID | Error: Selected Label Name not valid |
| **1021** | AQVI_SELECT_RANGE_ERROR | Error: Selected Range Condition Error, can't mix Line and Cursor Range condition |
| **1022** | AQVI_SELECT_CHANNEL_NAME_INVALID | Error: Selected Channel Name in Cursor Search is not valid |
| **1023** | AQVI_CURSOR_SEARCH_FAILED | Error: Cursor Search failed, unable to find more valid match |
| **1024** | AQVI_WAVEFORM_NOT_READY | Error: Waveform data not ready |
| **1025** | AQVI_NOT_IN_EV_MODE | Error: Software is not configured in EV mode|
| **1026** | AQVI_NO_EV_ANALYSIS_RESULT | Error: Software doesn't have any valid EV analysis result |
| **1027** | AQVI_SELECT_DEV_NOT_EXIST | Error: Selected Device S/N not presented in device list |
| **9995** | AQVI_UNSUPPORT_FEATURE | Error: Unsupported feature |
| **9996** | AQVI_UNFINISHED_FEATURE | Error: Unfinished Feature |
| **9997** | AQVI_UNKNOWN_COMMAND_ERROR | Error: Unknown command |
| **9998** | AQVI_UNKNOWN_ERROR | Error: Unknown Error |
