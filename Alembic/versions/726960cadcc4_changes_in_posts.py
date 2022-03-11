"""changes in posts

Revision ID: 726960cadcc4
Revises: 
Create Date: 2022-03-09 01:05:03.611300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726960cadcc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'owner_id')
    # ### end Alembic commands ###
