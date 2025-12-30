from __future__ import annotations

from typing import Sequence

from models.user import User


def select_top_users_by_rate(users: Sequence[User], top_size: int) -> list[User]:
    """Выбрать топ-N пользователей с максимальным рейтингом."""
    if top_size <= 0:
        return []
    ordered = sorted(list(users), key=lambda u: u.rate, reverse=True)
    return ordered[:top_size]
