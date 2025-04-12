from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.base_class import Base
from app.models.user import User
from app.models.task import Task


def init_db() -> None:
    engine = create_engine(settings.get_database_url)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # Create initial admin user if not exists
    admin_user = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin_user:
        admin_user = User(
            email="admin@example.com",
            auth0_id="auth0|admin",
            role="admin",
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)

    # Create initial manager user if not exists
    manager_user = db.query(User).filter(User.email == "manager@example.com").first()
    if not manager_user:
        manager_user = User(
            email="manager@example.com",
            auth0_id="auth0|manager",
            role="manager",
            is_active=True
        )
        db.add(manager_user)
        db.commit()
        db.refresh(manager_user)

    # Create initial regular user if not exists
    regular_user = db.query(User).filter(User.email == "user@example.com").first()
    if not regular_user:
        regular_user = User(
            email="user@example.com",
            auth0_id="auth0|user",
            role="user",
            is_active=True
        )
        db.add(regular_user)
        db.commit()
        db.refresh(regular_user)

    db.close()


if __name__ == "__main__":
    init_db() 