from contextlib import contextmanager
from database import SessionLocal

@contextmanager
def session_scope():
    db = SessionLocal()

    try:
        yield db
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
