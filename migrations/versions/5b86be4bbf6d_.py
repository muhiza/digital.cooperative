"""empty message

Revision ID: 5b86be4bbf6d
Revises: db7c27ff7144
Create Date: 2018-08-09 09:10:17.918081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b86be4bbf6d'
down_revision = 'db7c27ff7144'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('Code', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'Code')
    # ### end Alembic commands ###