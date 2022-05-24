from app.models.mahasiswa import Mahasiswa
from app.config.db import database

from fastapi.exceptions import HTTPException
from fastapi import Response


async def delete_mahasiswa(id: int):
    check_id_query = Mahasiswa.select(
        Mahasiswa.c.id_mahasiswa).where(Mahasiswa.c.id_mahasiswa == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Mahasiswa tidak ditemukan')

    query = Mahasiswa.delete().where(Mahasiswa.c.id_mahasiswa == id)
    await database.execute(query)

    return Response(status_code=204)
