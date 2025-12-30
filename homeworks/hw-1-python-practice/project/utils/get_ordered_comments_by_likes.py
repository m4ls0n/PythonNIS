from __future__ import annotations

from typing import Sequence

from models.comment import Comment


def get_ordered_comments_by_likes(comments: Sequence[Comment]) -> list[Comment]:
    """Вернуть комментарии, отсортированные по количеству лайков (убывание)."""
    return sorted(list(comments), key=lambda c: c.like_count, reverse=True)
