import asyncio
import grpc
import aqvisa_pb2
import aqvisa_pb2_grpc

# Command List
command_list = [
    # b"*STB?",
    # b"*LA:CAPTURE:TRIGGERED?",
    # b"*LA:CAPTURE:PROGRESS?",
    b"*LA:CAPTURE:START",
]

address = "192.168.1.211:5025"

async def viSingleRequest(strCommand: bytes) -> None:
    async with grpc.aio.insecure_channel(address) as channel:
        stub = aqvisa_pb2_grpc.AqVISAStub(channel)

        # ViWrite Command
        # if command is valid, status_code == AQVI_NO_ERROR
        # if command is not valid, job_id will not be assigned 
        # and the command will not be executed.
        # status_code will be AQVI_COMMAND_FORMAT_ERROR
        response = await stub.ViWrite(aqvisa_pb2.ViWriteRequest(command=strCommand))
        job_id = response.job_id
        print(f"viWrite {strCommand}\n" +
              f"\t- Job ID: {job_id}\n"
              f"\t- Status Code: {response.status_code}")

        # Check if no error occurs
        if response.status_code != aqvisa_pb2.AQVI_STATUS.AQVI_NO_ERROR:
            return
        
        await asyncio.sleep(1)
    
        # Wait for the command finish executing
        # response returns the result of the viWrite command
        while True:
            response = await stub.ViGetCommandResult(aqvisa_pb2.ViGetCommandResultRequest(job_id=job_id))

            # If command still processing, status code will remain AQVI_PREVIOUS_CMD_PROCESSING
            # If it finishes its process, it will return other status code (refer to aqvisa.proto)
            # No error: AQVI_NO_ERROR, Error: other possibilities
            if response.status_code != aqvisa_pb2.AQVI_PREVIOUS_CMD_PROCESSING:
                print(f"viGetCommandResult\n" +
                      f"\t- Status Code: {response.status_code}")
                break
            await asyncio.sleep(3)
        
        # viRead
        # Query the result of the command if result exists
        response = await stub.ViRead(aqvisa_pb2.ViReadRequest(job_id=job_id))
        print(f"viRead\n" +
              f"\t- Status Code: {response.status_code}\n" +
              f"\t- Response: {response.command_response}")


def main() -> None:
    tasks = [viSingleRequest(command) for command in command_list]
    asyncio.run(asyncio.wait(tasks))


if __name__ == '__main__':
    main()