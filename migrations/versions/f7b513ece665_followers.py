"""followers

Revision ID: f7b513ece665
Revises: 2aa912c6d3ca
Create Date: 2020-06-15 21:05:34.843658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7b513ece665'
down_revision = '2aa912c6d3ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###
