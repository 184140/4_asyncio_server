import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 9090, loop=loop)

    writer.write(message.encode())
    print(f'{message} sent to server')

    data = await reader.read(100)
    print(f'{data.decode()} received')

    print('Зыкрываем сокет')
    writer.close()


message = input("Введите сообщение для сервера: ")
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
