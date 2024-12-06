from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from API.database import get_db, Base
from sqlalchemy import Column, Integer, String

app02 = APIRouter()

# 定义学生成绩模型
class StudentScoreFromView(Base):
    __tablename__ = 'StudentScoresWithTotalRank'

    student_id = Column(String, primary_key=True)
    stu_name = Column(String)
    total_score = Column(Integer)
    score_rank = Column(Integer)
    class_ = Column(String)  # 注意这里使用 class_ 而不是 class，因为 class 是 Python 的保留字

# 新模型，引用实际的 StudentScores 表
class StudentScore(Base):
    __tablename__ = 'StudentScores'
    student_id = Column(String, primary_key=True)
    stu_name = Column(String)
    total_score = Column(Integer)
    score_rank = Column(Integer)
    class_ = Column(String)  # 使用 class_ 避免与 Python 关键字冲突

# 获取学生成绩列表
@app02.get("/studentscores")
async def read_student_scores(db: Session = Depends(get_db)):
    try:
        scores = db.query(StudentScoreFromView).all()
        if scores:
            return {"success": True, "data": scores}
        else:
            return {"success": True, "data": [], "message": "No data available"}
    except Exception as e:
        return {"success": False, "message": "Failed to fetch scores", "error": str(e)}


from pydantic import BaseModel

# 定义用于接收学号列表的 Pydantic 模型
class StudentIds(BaseModel):
    student_ids: list

# 删除学生成绩
from fastapi import HTTPException

@app02.delete("/studentscores")
async def delete_student_scores(data: StudentIds, db: Session = Depends(get_db)):
    not_found_ids = []  # 用于存储不存在的学号
    try:
        for student_id in data.student_ids:  # 从模型中提取学号列表
            student_score = db.query(StudentScore).filter(StudentScore.student_id == student_id).first()
            if student_score:
                db.delete(student_score)
            else:
                not_found_ids.append(student_id)  # 如果学号不存在，添加到列表中
        if not_found_ids:
            raise HTTPException(status_code=404, detail=f"学号不存在: {', '.join(not_found_ids)}")
        db.commit()
        return {"success": True, "message": "删除成功"}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "删除失败", "error": str(e)}

# 定义用于接收学生信息的 Pydantic 模型
class StudentScoreModel(BaseModel):
    student_id: str
    stu_name: str
    total_score: int
    score_rank: int
    class_: str


# 添加学生成绩
@app02.post("/studentscores")
async def add_student_score(data: StudentScoreModel, db: Session = Depends(get_db)):
    try:
        # 检查学号是否已存在
        existing_student = db.query(StudentScore).filter(StudentScore.student_id == data.student_id).first()
        if existing_student:
            raise HTTPException(status_code=400, detail="学号已存在")

        # 添加新学生成绩
        new_student = StudentScore(
            student_id=data.student_id,
            stu_name=data.stu_name,
            total_score=data.total_score,
            score_rank=data.score_rank,
            class_=data.class_
        )
        db.add(new_student)
        db.commit()
        return {"success": True, "message": "添加成功"}
    except HTTPException as e:
        # 直接将HTTPException的详情返回给前端
        return {"success": False, "message": "添加失败", "error": str(e)}
    except Exception as e:
        db.rollback()
        return {"success": False, "message": "添加失败", "error": str(e)}