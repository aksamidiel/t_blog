"""followers

Revision ID: 2aa912c6d3ca
Revises: acba479e0def
Create Date: 2020-06-15 21:01:37.790559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa912c6d3ca'
down_revision = 'acba479e0def'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'author')
    # ### end Alembic commands ###
