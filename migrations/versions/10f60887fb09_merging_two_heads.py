"""merging two heads

Revision ID: 10f60887fb09
Revises: b0a39769dfaa, f90a1e9966f0
Create Date: 2023-02-11 22:06:30.198456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f60887fb09'
down_revision = ('b0a39769dfaa', 'f90a1e9966f0')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
