"""Create Tag Model

Revision ID: 3f93187687fc
Revises: 7b1ed0952639
Create Date: 2023-12-13 20:16:58.457652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f93187687fc'
down_revision = '7b1ed0952639'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    # ### end Alembic commands ###
