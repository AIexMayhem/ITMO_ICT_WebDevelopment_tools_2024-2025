"""tag added

Revision ID: a128a7b90b22
Revises: 
Create Date: 2025-04-24 15:14:38.255557

"""
from typing import Sequence, Union
import sqlmodel

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a128a7b90b22'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('tag', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'tag')
    # ### end Alembic commands ###
