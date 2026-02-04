from database.models import ShortURL
from exceptions import ShortenerError, SlugAlreadyExistsError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def add_slug_to_db(
        slug: str,
        long_url: str,
        session: AsyncSession
):
    new_slug = ShortURL(
        slug=slug,
        long_url=long_url,
        session=AsyncSession
    )
    session.add(new_slug)
    try:
        await session.commit()
    except ShortenerError:
        raise SlugAlreadyExistsError


async def get_long_url_by_slug_from_db(slug: str, session: AsyncSession):
    query = select(ShortURL).filter_by(slug=slug)
    result = await session.execute(query)
    res: ShortURL | None = result.scalar_one_or_none()
    return res.long_url if res else None
