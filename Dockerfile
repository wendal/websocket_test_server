FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY websocket_server.py .

# 安装依赖
RUN pip install websockets

# 暴露端口
EXPOSE 8766

# 启动服务器
CMD ["python", "websocket_server.py"]