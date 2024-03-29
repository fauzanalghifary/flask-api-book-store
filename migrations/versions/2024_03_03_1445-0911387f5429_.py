"""empty message

Revision ID: 0911387f5429
Revises: 
Create Date: 2024-03-03 14:45:51.101010

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0911387f5429'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=80), nullable=False),
                    sa.Column('author', sa.String(length=80), nullable=False),
                    sa.Column('price', sa.Numeric(precision=10, scale=3), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('title')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
