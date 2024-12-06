from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from API.database import get_db, Base
from sqlalchemy import Column, String, Integer

app04 = APIRouter()

# 定义班级信息模型
class ClassInfo(Base):
    __tablename__ = 'ClassInfo'
    class_id = Column(String(40), primary_key=True, nullable=False)
    cls_rank = Column(String(40), nullable=False)
    head_teacher = Column(String(40), nullable=False)
    student_count = Column(Integer, nullable=False)

# 定义班级信息视图模型
class ViewClassInfo(Base):
    __tablename__ = 'ViewClassInfo'
    class_id = Column(String(40), primary_key=True)
    cls_rank = Column(String(40))
    head_teacher = Column(String(40))
    student_count = Column(Integer)

# 获取班级信息列表
@app04.get("/classes")
async def read_classes(db: Session = Depends(get_db)):
    try:
        classes = db.query(ViewClassInfo).all()
        if classes:
            return {"success": True, "data": classes}
        else:
            return {"success": True, "data": [], "message": "No data available"}
    except Exception as e:
        return {"success": False, "message": "Failed to fetch classes", "error": str(e)}


from pydantic import BaseModel

# 定义用于接收班级ID列表的 Pydantic 模型
class ClassIds(BaseModel):
    class_ids: list

# 删除班级信息
@app04.delete("/classes")
async def delete_classes(data: ClassIds, db: Session = Depends(get_db)):
    not_found_ids = []  # 用于存储不存在的班级ID
    try:
        for class_id in data.class_ids:  # 从模型中提取班级ID列表
            class_info = db.query(ClassInfo).filter(ClassInfo.class_id == class_id).first()
            if class_info:
                db.delete(class_info)
            else:
                not_found_ids.append(class_id)  # 如果班级ID不存在，添加到列表中
        if not_found_ids:
            raise HTTPException(status_code=404, detail=f"班级ID不存在: {', '.join(not_found_ids)}")
        db.commit()
        return {"success": True, "message": "删除成功"}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "删除失败", "error": str(e)}


# 定义用于接收班级信息的 Pydantic 模型
class ClassInfoModel(BaseModel):
    class_id: str
    cls_rank: str
    head_teacher: str
    student_count: int

# 添加班级信息
@app04.post("/classes")
async def add_class(data: ClassInfoModel, db: Session = Depends(get_db)):
    try:
        # 检查班级ID是否已存在
        existing_class = db.query(ClassInfo).filter(ClassInfo.class_id == data.class_id).first()
        if existing_class:
            raise HTTPException(status_code=400, detail="班级ID已存在")

        # 添加新班级信息
        new_class = ClassInfo(
            class_id=data.class_id,
            cls_rank=data.cls_rank,
            head_teacher=data.head_teacher,
            student_count=data.student_count
        )
        db.add(new_class)
        db.commit()
        return {"success": True, "message": "添加成功"}
    except HTTPException as e:
        # 直接将HTTPException的详情返回给前端
        return {"success": False, "message": "添加失败", "error": str(e)}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "添加失败", "error": str(e)}