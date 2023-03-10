"""add content column to posts table

Revision ID: 01218e3d78f9
Revises: 7a8978075ffa
Create Date: 2023-03-08 13:00:36.652664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01218e3d78f9'
down_revision = '7a8978075ffa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
