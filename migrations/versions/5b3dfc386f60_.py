"""empty message

Revision ID: 5b3dfc386f60
Revises: f30737d894db
Create Date: 2022-10-31 23:40:53.333347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b3dfc386f60'
down_revision = 'f30737d894db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###
