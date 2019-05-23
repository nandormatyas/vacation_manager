"""vacations table

Revision ID: a76043764481
Revises: fcc3bc594699
Create Date: 2019-05-21 14:50:12.533321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a76043764481'
down_revision = 'fcc3bc594699'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('fromDate', sa.Date(), nullable=True),
    sa.Column('toDate', sa.Date(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacation')
    # ### end Alembic commands ###
