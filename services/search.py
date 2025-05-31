from sqlalchemy.orm import Session
from models.db import Paper
from schemas.paper import PaperCreate

def store_search_result(db: Session, paper: PaperCreate) -> Paper:
    """
    논문 검색 결과를 데이터베이스에 저장합니다.
    이미 같은 논문이 존재하면 중복 저장을 방지하고 기존 데이터를 반환합니다.
    중복 기준은 link_url 또는 (title + pub_date)입니다.
    """
    # 중복 체크: 링크 또는 (제목 + 날짜)
    existing = db.query(Paper).filter(
        (Paper.link_url == paper.link_url) |
        ((Paper.title == paper.title) & (Paper.pub_date == paper.pub_date))
    ).first()
    if existing:
        return existing

    # authors는 JSON 필드이므로 리스트 그대로 저장
    db_paper = Paper(
        title=paper.title,
        authors=paper.authors,  # ["홍길동", "김철수"]
        journal=paper.journal,
        pub_date=paper.pub_date,
        link_url=paper.link_url
    )
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper
