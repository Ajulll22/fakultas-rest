from sqlalchemy import (
    Column,
    ForeignKey,
    Text,
    Integer,
    String,
    Table
)
from app.config.db import metadata


Mahasiswa = Table(
    'mahasiswa',
    metadata,
    Column('id_mahasiswa', Integer, primary_key=True),
    Column('npm_mahasiswa', String(255)),
    Column('nama_mahasiswa', String(255)),
    Column('id_jurusan', Integer, ForeignKey('jurusan.id_jurusan'))
)
