from sqlalchemy import (
    Column,
    Text,
    Integer,
    String,
    Table
)
from app.config.db import metadata

Jurusan = Table(
    'jurusan',
    metadata,
    Column('id_jurusan', Integer, primary_key=True),
    Column('nama_jurusan', String(255)),
    Column('deskripsi', Text)
)
