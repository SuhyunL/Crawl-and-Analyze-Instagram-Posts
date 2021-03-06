"""empty message

Revision ID: e1c4aa44249c
Revises: 686fceba301d
Create Date: 2021-03-29 16:43:38.731458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1c4aa44249c'
down_revision = '686fceba301d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('crawler', 'caption')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crawler', sa.Column('caption', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
