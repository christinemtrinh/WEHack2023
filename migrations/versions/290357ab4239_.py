"""empty message

Revision ID: 290357ab4239
Revises: 10f60887fb09
Create Date: 2023-02-11 22:21:04.717519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290357ab4239'
down_revision = '10f60887fb09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('contentID', sa.Integer(), nullable=False),
    sa.Column('time_done', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'username', 'contentID')
    )
    with op.batch_alter_table('user_history', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_history_username'), ['username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_history', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_history_username'))

    op.drop_table('user_history')
    # ### end Alembic commands ###
