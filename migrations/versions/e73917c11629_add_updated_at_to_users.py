"""add updated_at to users

Revision ID: e73917c11629
Revises: 66e9c9663fe9
Create Date: 2026-04-08 12:25:18.502049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e73917c11629'
down_revision: Union[str, Sequence[str], None] = '66e9c9663fe9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Adiciona a coluna updated_at à tabela users."""
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), 
                  server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))


def downgrade() -> None:
    """Remove a coluna updated_at da tabela users."""
    op.drop_column('users', 'updated_at')