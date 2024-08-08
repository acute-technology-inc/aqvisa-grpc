import asyncio
import grpc
import aqvisa_pb2
import aqvisa_pb2_grpc
import json


# TODO: Replace this with your own setup
address = "<address>:<ip>"
json_file = "<filepath>"

async def viSingleReadFileRequest() -> None:
    async with grpc.aio.insecure_channel(address) as channel:
        stub = aqvisa_pb2_grpc.AqVISAStub(channel)

        # ViReadToFile Command
        # if the file is successfully transferred
        # status_code == AQVI_NO_ERROR
        response = await stub.ViReadToFile(
            aqvisa_pb2.ViReadToFileRequest(
                schema_type=aqvisa_pb2.AQVI_JSON_SCHEMA_ELECTRICAL_VALIDATION,
                count=200_000
            )
        )
    
        print(f"viReadToFile\n" +
              f"\t- Status Code: {response.status_code}\n" +
              f"\t- Return Count: {response.ret_count}")

        data = json.loads(response.payload.decode())
    
        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)


async def main() -> None:
    tasks = [asyncio.create_task(viSingleReadFileRequest())]
    _, _ = await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
