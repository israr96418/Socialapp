"""delete phone number to post

Revision ID: 67409ce5c67d
Revises: 2d0909e263ff
Create Date: 2022-03-11 12:29:26.762726

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '67409ce5c67d'
down_revision = '2d0909e263ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('phone', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
