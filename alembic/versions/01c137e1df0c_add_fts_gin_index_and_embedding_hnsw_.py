"""add fts gin index and embedding hnsw index

Revision ID: 01c137e1df0c
Revises: e42ff3d4b3bf
Create Date: 2026-09-26 23:28:12.184671

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01c137e1df0c'
down_revision: Union[str, Sequence[str], None] = 'e42ff3d4b3bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Lexical search computed to_tsvector('french', content) inline with no
    # index behind it, forcing a full-table scan + tsvector computation on
    # every query. Functional GIN index matches that exact expression.
    op.execute(
        "CREATE INDEX ix_document_chunk_content_fts "
        "ON document_chunk USING GIN (to_tsvector('french', content))"
    )
    # Semantic search orders by cosine_distance with no ANN index, so it
    # also does a full sequential scan + distance computation per query.
    # HNSW (no upfront list-count tuning needed, unlike ivfflat) with the
    # cosine op class to match DocumentChunk.embedding.cosine_distance().
    op.execute(
        "CREATE INDEX ix_document_chunk_embedding_hnsw "
        "ON document_chunk USING hnsw (embedding vector_cosine_ops)"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP INDEX IF EXISTS ix_document_chunk_embedding_hnsw")
    op.execute("DROP INDEX IF EXISTS ix_document_chunk_content_fts")
