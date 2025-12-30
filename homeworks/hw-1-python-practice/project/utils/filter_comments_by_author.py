from __future__ import annotations

from typing import Sequence

from models.comment import Comment
from models.user import User


def filter_comments_by_author(comments: Sequence[Comment], author: User) -> list[Comment]:
    """Оставить только комментарии, написанные указанным пользователем."""
    return [c for c in comments if c.author_id == author.id]
