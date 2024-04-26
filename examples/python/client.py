import asyncio
import grpc
import aqvisa_pb2
import aqvisa_pb2_grpc

# Command List
command_list = [
    b"*IDN?",
    # b"*LA:CAPTURE:START"
    # b"*LA:CAPTURE:TRIGGERED?",
    # b"*LA:CAPTURE:PROGRESS?",
]

# TODO: Replace this with your own setup
address = "<address>:<ip>"

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
        
        # viRead
        # Query the result of the command if result exists
        response = await stub.ViRead(aqvisa_pb2.ViReadRequest(count=200_000_000))
        print(f"viRead\n" +
              f"\t- Status Code: {response.status_code}\n" +
              f"\t- Return Count: {response.ret_count}\n" +
              f"\t- Response: {response.command_response}")


def main() -> None:
    tasks = [viSingleRequest(command) for command in command_list]
    asyncio.run(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
