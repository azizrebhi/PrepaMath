"""add part_id link on document_parent_chunk

Revision ID: 688ce9a92b86
Revises: 01c137e1df0c
Create Date: 2026-09-27 20:57:57.543082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '688ce9a92b86'
down_revision: Union[str, Sequence[str], None] = '01c137e1df0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "document_parent_chunk",
        sa.Column("part_id", sa.UUID(), nullable=True),
    )
    op.create_foreign_key(
        "fk_document_parent_chunk_part_id",
        "document_parent_chunk",
        "chapter_part",
        ["part_id"],
        ["id"],
    )
    op.create_index(
        op.f("ix_document_parent_chunk_part_id"),
        "document_parent_chunk",
        ["part_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_document_parent_chunk_part_id"), table_name="document_parent_chunk")
    op.drop_constraint(
        "fk_document_parent_chunk_part_id", "document_parent_chunk", type_="foreignkey"
    )
    op.drop_column("document_parent_chunk", "part_id")
