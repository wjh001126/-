from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库连接字符串
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost/datas"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建会话本地工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建声明式基类
Base = declarative_base()

# 定义用户模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    registration_date = Column(DateTime)
    is_admin = Column(Boolean, default=False)  # 添加一个字段来判断是否为管理员

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建一个依赖项函数来管理数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()