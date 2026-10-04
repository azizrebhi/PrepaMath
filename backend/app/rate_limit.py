import os

from slowapi import Limiter
from slowapi.util import get_remote_address

# Keyed by IP rather than user_id — simpler (no JWT decoding needed inside
# the key function), and good enough for a portfolio-scale deployment. The
# daily token budget in answer.py is the real cost-control layer; this just
# stops rapid-fire bursts. Falls back to in-memory storage if REDIS_URL isn't
# set (fine for local dev with one process; a real multi-process deployment
# needs the Redis backend so limits are shared across workers).
limiter = Limiter(key_func=get_remote_address, storage_uri=os.getenv("REDIS_URL", "memory://"))
