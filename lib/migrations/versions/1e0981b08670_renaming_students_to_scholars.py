"""Renaming students to scholars

Revision ID: 1e0981b08670
Revises: 791279dd0760
Create Date: 2025-05-29 09:57:20.176751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e0981b08670'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
