from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal
from allAPI.LoginANDEnroll import app01
from allAPI.student_scores import app02
from allAPI.enrollment_api import app03
from allAPI.ClassInfo import app04

app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)


app.include_router(app01, prefix="/WJH", tags=["登录与注册"])
app.include_router(app02, prefix="/WJH", tags=["成绩信息"])
app.include_router(app03, prefix="/WJH", tags=["学籍信息"])
app.include_router(app04, prefix="/WJH", tags=["班级信息"])

# 定义生命周期事件处理器
async def shutdown_event(app: FastAPI) -> None:
    await SessionLocal.close_all()

# 注册事件处理器
app.add_event_handler("shutdown", shutdown_event)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True, host="127.0.0.1")
    # uvicorn.run("main:app", port=8000, reload=True, host="localhost")