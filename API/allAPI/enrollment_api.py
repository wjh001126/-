from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from API.database import get_db, Base
from sqlalchemy import Column, String, Date


# 创建API路由
app03 = APIRouter()


# 定义学生学籍信息模型
class StudentEnrollment(Base):
    __tablename__ = 'StudentEnrollment'

    student_id = Column(String(8), primary_key=True, nullable=False)
    stu_name = Column(String(8), nullable=False)
    gender = Column(String(6), nullable=False)
    class_ = Column(String(20), nullable=False)
    birth_date = Column(String(80), nullable=False)
    school = Column(String(200), nullable=False)

# 创建视图模型
class ViewStudentEnrollment(Base):
    __tablename__ = 'ViewStudentEnrollment'

    student_id = Column(String(8), primary_key=True)
    stu_name = Column(String(8))
    gender = Column(String(6))
    class_ = Column(String(20))
    birth_date = Column(String(80))
    school = Column(String(200))

# 定义用于接收学生信息的 Pydantic 模型
class StudentEnrollmentModel(BaseModel):
    student_id: str
    stu_name: str
    gender: str
    class_: str
    birth_date: str
    school: str

# 获取学生学籍信息列表
@app03.get("/enrollments")
async def read_enrollments(db: Session = Depends(get_db)):
    try:
        enrollments = db.query(ViewStudentEnrollment).all()
        if enrollments:
            return {"success": True, "data": enrollments}
        else:
            return {"success": True, "data": [], "message": "No data available"}
    except Exception as e:
        return {"success": False, "message": "Failed to fetch enrollments", "error": str(e)}


# 定义用于接收学号列表的 Pydantic 模型
class StudentIds(BaseModel):
    student_ids: list

# 删除学生学籍信息
@app03.delete("/enrollments")
async def delete_enrollments(data: StudentIds, db: Session = Depends(get_db)):
    not_found_ids = []  # 用于存储不存在的学号
    try:
        for student_id in data.student_ids:  # 从模型中提取学号列表
            enrollment = db.query(StudentEnrollment).filter(StudentEnrollment.student_id == student_id).first()
            if enrollment:
                db.delete(enrollment)
            else:
                not_found_ids.append(student_id)  # 如果学号不存在，添加到列表中
        if not_found_ids:
            raise HTTPException(status_code=404, detail=f"学号不存在: {', '.join(not_found_ids)}")
        db.commit()
        return {"success": True, "message": "删除成功"}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "删除失败", "error": str(e)}

# 添加学生学籍信息
@app03.post("/enrollments")
async def add_enrollment(data: StudentEnrollmentModel, db: Session = Depends(get_db)):
    try:
        # 检查学号是否已存在
        existing_enrollment = db.query(StudentEnrollment).filter(StudentEnrollment.student_id == data.student_id).first()
        if existing_enrollment:
            raise HTTPException(status_code=400, detail="学号已存在")

        # 添加新学生学籍信息
        new_enrollment = StudentEnrollment(
            student_id=data.student_id,
            stu_name=data.stu_name,
            gender=data.gender,
            class_=data.class_,
            birth_date=data.birth_date,
            school=data.school
        )
        db.add(new_enrollment)
        db.commit()
        return {"success": True, "message": "添加成功"}
    except HTTPException as e:
        # 直接将HTTPException的详情返回给前端
        return {"success": False, "message": "添加失败", "error": str(e)}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "添加失败", "error": str(e)}