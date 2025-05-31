from sqlalchemy.orm import Session
from models.db import Paper
from models.user import User as UserModel
from models.bookmark import Bookmark
from schemas.paper import PaperOut  # FastAPI 응답 직렬화를 위한 모델

def list_saved_papers(db: Session, user: UserModel) -> list[PaperOut]:
    """
    해당 사용자가 북마크한 논문 리스트를 반환합니다.
    Paper 객체 리스트를 그대로 반환하면 FastAPI에서 자동 직렬화됩니다.
    """
    bookmarks = db.query(Bookmark).filter_by(user_id=user.id).all()
    papers = [bm.paper for bm in bookmarks]
    return papers  # FastAPI 라우터에서 response_model=list[PaperOut]으로 처리
