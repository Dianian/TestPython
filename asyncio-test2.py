# 
# Created by 付博文 on 2017/10/10.
#

import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, write = yield from connect
    header = 'GET/HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    write.write(header.encode('utf-8'))
    yield from write.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    write.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
