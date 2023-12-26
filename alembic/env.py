from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context

config = context.config
fileConfig(config.config_file_name)
target_metadata = None

def run_migrations_online():
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()

run_migrations_online()
