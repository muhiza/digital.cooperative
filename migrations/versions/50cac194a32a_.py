"""empty message

Revision ID: 50cac194a32a
Revises: 
Create Date: 2018-10-07 08:58:42.970797

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '50cac194a32a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('umusaruro', sa.Column('members_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'umusaruro', 'members', ['members_id'], ['id'])
    op.drop_column('umusaruro', 'membersss_id')
    op.drop_column('umusaruro', 'member_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('umusaruro', sa.Column('member_id', mysql.VARCHAR(length=200), nullable=True))
    op.add_column('umusaruro', sa.Column('membersss_id', mysql.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'umusaruro', type_='foreignkey')
    op.drop_column('umusaruro', 'members_id')
    # ### end Alembic commands ###
