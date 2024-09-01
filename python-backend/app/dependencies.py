from app.database import SessionLocal


# FastAPI injection to get the current database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()