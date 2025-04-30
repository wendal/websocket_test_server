# WebSocket Test Server

一个简单的WebSocket测试服务器，支持echo和随机字符串生成功能。

## 功能特点

- Echo服务：将接收到的消息原样返回
- 随机字符串生成：根据指定大小生成随机字符串
- 支持大数据量：随机字符串最大支持64KB-1（65535字节）
- Docker支持：提供容器化部署方案

## 安装

### 直接运行

1. 确保已安装Python 3.x
2. 安装依赖：
```bash
pip install websockets
```
3. 运行服务器：
```bash
python websocket_server.py
```

### Docker方式

```bash
# 拉取镜像
docker pull wendal/websocket_test_server:1.0.1

# 运行容器
docker run -p 8080:8080 wendal/websocket_test_server:1.0.1
```

## API使用说明

服务器默认监听在 `ws://localhost:8080`

### Echo模式

直接发送任意文本消息，服务器将原样返回。

示例：
```javascript
// JavaScript WebSocket客户端示例
const ws = new WebSocket('ws://localhost:8080');
ws.onopen = () => {
    ws.send('Hello, WebSocket!');
};
ws.onmessage = (event) => {
    console.log('收到消息:', event.data); // 输出: Hello, WebSocket!
};
```

### 随机字符串生成

发送JSON格式消息，包含`echosize`参数指定需要生成的随机字符串长度。

参数说明：
- `echosize`: 整数，范围1-65535（64KB-1）

示例：
```javascript
// 请求10字节随机字符串
ws.send(JSON.stringify({
    echosize: 10
}));

// 服务器将返回10个随机字符，例如："aB3kP9mN2x"
```

错误处理：
- 如果`echosize`参数无效，将返回错误信息：
```json
{
    "error": "echosize must be an integer between 1 and 65535"
}
```

## Docker镜像

镜像托管在以下位置：

- Docker Hub: `wendal/websocket_test_server`
- GitHub Packages: `ghcr.io/wendal/websocket_test_server`

支持的标签：
- `1.0.1`: 当前稳定版本
- `latest`: 最新版本

## 许可证

本项目基于LICENSE文件中规定的许可条款发布。