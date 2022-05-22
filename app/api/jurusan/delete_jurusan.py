from app.models.jurusan import Jurusan
from app.config.db import database

from fastapi.exceptions import HTTPException
from fastapi import Response


async def delete_jurusan(id: int):
    check_id_query = Jurusan.select(
        Jurusan.c.id_jurusan).where(Jurusan.c.id_jurusan == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Jurusan tidak ditemukan')

    query = Jurusan.delete().where(Jurusan.c.id_jurusan == id)
    await database.execute(query)

    return Response(status_code=204)
