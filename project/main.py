from fastapi import FastAPI
from app.routers import posts, comments
from app.database import Base, engine

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()


# 라우터 등록
app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(comments.router, prefix="/api/comments", tags=["comments"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Board"}

