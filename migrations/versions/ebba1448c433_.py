"""empty message

Revision ID: ebba1448c433
Revises: 149ee9158d0b
Create Date: 2018-09-09 18:41:54.978042

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ebba1448c433'
down_revision = '149ee9158d0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('tariki_yavukiye', sa.String(length=200), nullable=True))
    op.drop_column('members', 'tariki_yamavuko')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('tariki_yamavuko', mysql.VARCHAR(length=200), nullable=True))
    op.drop_column('members', 'tariki_yavukiye')
    # ### end Alembic commands ###