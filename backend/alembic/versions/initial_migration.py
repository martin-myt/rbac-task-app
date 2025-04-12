"""initial migration

Revision ID: initial
Revises: 
Create Date: 2024-03-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('auth0_id', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('role', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('auth0_id')
    )

    # Create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='todo'),
        sa.Column('assigned_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['assigned_user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.CheckConstraint("status IN ('todo', 'in_progress', 'done')")
    )


def downgrade() -> None:
    op.drop_table('tasks')
    op.drop_table('users') 