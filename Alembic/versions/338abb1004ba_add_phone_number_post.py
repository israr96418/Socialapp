"""add_phone_number_post

Revision ID: 338abb1004ba
Revises: 67409ce5c67d
Create Date: 2022-03-13 21:44:50.284032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '338abb1004ba'
down_revision = '67409ce5c67d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=20), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###
