"""order payment method

Revision ID: 5b2b6fdf3878
Revises: c4f1701d3a7b
Create Date: 2024-11-17 00:02:43.267906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2b6fdf3878'
down_revision = 'c4f1701d3a7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('Payment method', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'Payment method')
    # ### end Alembic commands ###
