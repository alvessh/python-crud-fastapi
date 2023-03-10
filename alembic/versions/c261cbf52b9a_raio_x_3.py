"""RAIO X - 3

Revision ID: c261cbf52b9a
Revises: 956c393d220a
Create Date: 2023-03-04 16:29:04.231251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c261cbf52b9a'
down_revision = '956c393d220a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('gameDate', sa.String(), nullable=True))
    op.add_column('game', sa.Column('addres', sa.String(), nullable=True))
    op.drop_column('game', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('game', 'addres')
    op.drop_column('game', 'gameDate')
    # ### end Alembic commands ###
