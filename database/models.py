from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

class ShortURL(Base):
    __tablename__ = 'short_urls'

    slug: Mapped[str] = mapped_column(primary_key=True)
    long_url: Mapped[str]
