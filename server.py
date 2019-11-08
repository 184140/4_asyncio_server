import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message} from {addr}")

    writer.write(data)
    await writer.drain()
    print(f"{data} sent back")

    writer.close()
    print("Client socket closed")


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 9090, loop=loop)
server = loop.run_until_complete(coro)

# работает, пока не нажмём Ctrl+C
print(f'Server based on {server.sockets[0].getsockname()}')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# закрываем сервер
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
