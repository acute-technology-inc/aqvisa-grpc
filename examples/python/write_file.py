import asyncio
import grpc
import aqvisa_pb2
import aqvisa_pb2_grpc
import json


# TODO: Replace this with your own setup
address = "<address>:<ip>"
json_file = "<filepath>"

async def viSingleWriteFileRequest() -> None:
    async with grpc.aio.insecure_channel(address) as channel:
        stub = aqvisa_pb2_grpc.AqVISAStub(channel)

        # ViWriteFromFile Command
        # if the file is successfully transferred
        # status_code == AQVI_NO_ERROR
        with open(json_file, "r") as f:
            payload = json.dumps(json.load(f)).encode()

            response = await stub.ViWriteFromFile(
                aqvisa_pb2.ViWriteFromFileRequest(payload=payload)
            )

            print(f"viWriteFromFile\n" +
                  f"\t- Status Code: {response.status_code}")


async def main() -> None:
    tasks = [asyncio.create_task(viSingleWriteFileRequest())]
    _, _ = await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
