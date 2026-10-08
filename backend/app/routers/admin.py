"""Temporary admin router — exists solely to run ingestion from inside Render,
where the database connection is already proven to work, bypassing a local
machine's broken path to Supabase (see conversation history: TCP connects
fine, but the SSL/protocol handshake silently hangs on every local network
tried, while Render's own connection has never had this problem).

Delete this file (and its registration in main.py) once the three chapters
are ingested — it is not meant to be a permanent part of the API surface.
"""

import os
import tempfile

from fastapi import APIRouter, BackgroundTasks, Header, HTTPException
from pydantic import BaseModel

from task import ingest_markdown_file

router = APIRouter(prefix="/admin", tags=["admin"])


class IngestRequest(BaseModel):
    title: str
    content: str


async def _run_ingest(temp_path: str, title: str):
    try:
        await ingest_markdown_file(temp_path, title)
    finally:
        os.unlink(temp_path)


@router.post("/ingest")
async def ingest(
    payload: IngestRequest,
    background_tasks: BackgroundTasks,
    x_admin_secret: str = Header(...),
):
    expected = os.getenv("ADMIN_INGEST_SECRET")
    if not expected or x_admin_secret != expected:
        raise HTTPException(status_code=403, detail="Forbidden")

    # Ingestion takes several minutes (one OpenAI call per structural unit
    # for contextual summaries, ~100-200+ units per chapter) — run it in the
    # background instead of blocking the response, since Cloudflare (sitting
    # in front of Render) kills proxied connections around 100s and the
    # request would be cut off long before ingestion finishes.
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(payload.content)
        temp_path = f.name

    background_tasks.add_task(_run_ingest, temp_path, payload.title)
    return {"status": "started", "title": payload.title}
