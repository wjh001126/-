from fastapi import FastAPI, HTTPException, status, Request, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from API.database import SessionLocal, User, get_db  # 从 database.py 导入 SessionLocal, User 和 get_db



from sqlalchemy.orm import Session
from datetime import datetime


app01 = APIRouter()


# # 创建数据库连接字符串
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost/datas"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
#
# # 创建会话本地工厂
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # 创建声明式基类
# Base = declarative_base()


# 定义用户模型
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True)
#     password = Column(String(50))
#     registration_date = Column(DateTime)
#     is_admin = Column(Boolean, default=False)  # 添加一个字段来判断是否为管理员


# 创建数据库表
# Base.metadata.create_all(bind=engine)


# # 创建一个依赖项函数来管理数据库会话
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# 用户登录请求模型
class Login(BaseModel):
    username: str
    password: str


# 登录接口
@app01.post("/login")
async def login(login: Login, db: Session = Depends(get_db)):
    if not login.username or not login.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户名和密码不能为空")

    # session = SessionLocal()
    user = db.query(User).filter(User.username == login.username).first()

    if user and user.password == login.password:
        return {"success": True, "user_type": "admin" if user.is_admin else "user"}
    else:
        return {"success": False}  # 返回一个标准的 JSON 响应


# 用户注册请求模型
class Register(BaseModel):
    username: str
    password: str


# 然后在路由函数中使用这个依赖项
@app01.post("/register")
async def register(user: Register, db: Session = Depends(get_db)):
    # 检查用户是否已存在
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        return {"success": False, "message": "用户已存在"}

    # 创建新用户
    new_user = User(
        username=user.username,
        password=user.password,  # 在实际应用中，应该对密码进行哈希处理
        registration_date=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success": True, "message": "注册成功", "user_id": new_user.id}










# # 定义生命周期事件处理器，事件处理器不能写在这
# async def shutdown_event(app: FastAPI) -> None:
#     await SessionLocal.close_all()
#
#
# # 注册事件处理器
# app01.add_event_handler("shutdown", shutdown_event)

# # 运行应用
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="localhost", port=8000)
#     # uvicorn.run(app, host="localhost", port=63342)
