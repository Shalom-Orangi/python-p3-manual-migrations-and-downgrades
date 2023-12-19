"""Renaming students to scholars

Revision ID: b9d1061f87b8
Revises: 791279dd0760
Create Date: 2023-12-20 00:24:05.474638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9d1061f87b8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
