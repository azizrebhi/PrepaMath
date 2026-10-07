import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from app.model import Base

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# alembic.ini's sqlalchemy.url is a local-dev-only placeholder
# (postgresql+psycopg2://prepamath:prepamath@localhost:5432/prepamath) — it
# only ever worked because a real local Postgres happened to be listening
# there with those exact credentials. Override it with the real postgres_url
# env var (the same one app/database.py reads) whenever it's set, so
# migrations target whatever database is actually configured instead of
# always connecting to localhost regardless of environment. Alembic runs
# synchronously here, so the +asyncpg driver from postgres_url (meant for
# the app's async engine) is swapped for +psycopg2, already a dependency
# for exactly this purpose.
database_url = os.getenv("postgres_url")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url.replace("+asyncpg", "+psycopg2"))

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
