from fastapi import FastAPI, Form, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse
import secrets

app = FastAPI()
security = HTTPBasic()

# 질문을 저장할 리스트 초기화
questions = []
users = {"admin": "password123"}  # 샘플 사용자 데이터 (아이디, 비밀번호)

class Question(BaseModel):
    question_id: int
    user_name: str
    subject: str
    question_text: str
    answer: Optional[str] = None

# 로그인 인증 함수
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, users.get(credentials.username, ""))
    if not (correct_username and correct_password):
        return None
    return credentials.username

@app.get("/", response_class=HTMLResponse)
async def get_question_form():
    html_content = """
    <html>
        <head>
            <title>질문 게시판</title>
        </head>
        <body>
            <h1>질문 게시판</h1>
            <form action="/submit_question" method="post">
                <label>아이디:</label><br>
                <input type="text" name="user_name" placeholder="아이디 입력"><br><br>
                <label>과목명:</label><br>
                <input type="text" name="subject" placeholder="과목 입력"><br><br>
                <label>질문:</label><br>
                <textarea name="question_text" rows="4" cols="50" placeholder="질문을 입력하세요"></textarea><br><br>
                <input type="submit" value="질문 등록">
            </form>
            <hr>
            <h2>질문 목록</h2>
            <ul>
    """
    # 저장된 질문 출력
    for question in questions:
        html_content += f"""
            <li>
                <b>질문 ID:</b> {question['question_id']}<br>
                <b>아이디:</b> {question['user_name']}<br>
                <b>과목명:</b> {question['subject']}<br>
                <b>질문:</b> {question['question_text']}<br>
                <b>답변:</b> {question['answer'] if question['answer'] else '답변 대기 중'}<br>
                <hr>
            </li>
        """
    html_content += """
            </ul>
        </body>
    </html>
    """
    return html_content

@app.post("/submit_question")
async def submit_question(user_name: str = Form(...), subject: str = Form(...), question_text: str = Form(...)):
    question_id = len(questions) + 1
    question = {
        "question_id": question_id,
        "user_name": user_name,
        "subject": subject,
        "question_text": question_text,
        "answer": None
    }
    questions.append(question)
    return {"message": "질문이 등록되었습니다.", "question_id": question_id}

@app.post("/answer_question")
async def answer_question(credentials: HTTPBasicCredentials = Depends(security),
                          question_id: int = Form(...), answer: str = Form(...)):
    current_user = get_current_user(credentials)
    if not current_user:
        return {"error": "로그인이 필요합니다."}

    for question in questions:
        if question['question_id'] == question_id:
            question['answer'] = answer
            return {"message": f"질문 ID {question_id}에 대한 답변이 등록되었습니다."}
    return {"error": "해당 ID의 질문을 찾을 수 없습니다."}
