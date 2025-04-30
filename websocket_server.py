import asyncio
import json
import random
import string
import websockets

async def handle_message(websocket):
    """处理WebSocket连接的消息"""
    try:
        async for message in websocket:
            try:
                # 解析JSON数据
                data = json.loads(message)
                
                # 检查是否存在echosize字段
                if 'echosize' in data:
                    size = data['echosize']
                    
                    # 验证size是否为整数且在有效范围内
                    if isinstance(size, int) and 0 < size < 16384:
                        # 生成随机字符串
                        random_string = ''.join(random.choices(
                            string.ascii_letters + string.digits, 
                            k=size
                        ))
                        
                        # 发送随机字符串
                        await websocket.send(random_string)
                    else:
                        await websocket.send(json.dumps({
                            "error": "echosize must be an integer between 1 and 16383"
                        }))
                else:
                    await websocket.send(json.dumps({
                        "error": "missing echosize field"
                    }))
                    
            except json.JSONDecodeError:
                await websocket.send(json.dumps({
                    "error": "invalid JSON format"
                }))
                
    except websockets.exceptions.ConnectionClosed:
        pass

async def main():
    """启动WebSocket服务器"""
    server = await websockets.serve(
        handle_message,
        "0.0.0.0",  # 监听所有网络接口
        8766        # 端口号
    )
    print("WebSocket server started on ws://0.0.0.0:8766")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())