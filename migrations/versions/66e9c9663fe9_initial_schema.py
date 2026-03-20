"""initial_schema

Revision ID: 66e9c9663fe9
Revises: c2559533f277
Create Date: 2026-03-20 10:02:06.836348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66e9c9663fe9'
down_revision: Union[str, Sequence[str], None] = 'c2559533f277'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
