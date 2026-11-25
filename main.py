from fastapi import FastAPI
from pydantic import BaseModel

# 1. 创建 FastAPI 应用实例
app = FastAPI(title="My First AI FDE Backend")

# 2. 用 Pydantic 定义请求的数据结构（类似 C++ 的 struct）
class EchoRequest(BaseModel):
    message: str          # 必填字段，必须是字符串
    repeat_times: int = 1 # 选填字段，必须是整数，如果不传默认为 1

# 3. 定义 GET 接口：健康检查
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running smoothly!"}

# 4. 定义 POST 接口：接收 JSON 数据并返回处理结果
@app.post("/echo")
def echo_message(payload: EchoRequest):
    # payload 已经被自动校验并转换成了 EchoRequest 对象，可以直接用点号访问属性
    result = (payload.message + " ") * payload.repeat_times
    return {
        "received_message": payload.message,
        "repeat_times": payload.repeat_times,
        "output": result.strip()
    }

