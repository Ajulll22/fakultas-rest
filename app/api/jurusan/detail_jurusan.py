from app.api_models import BaseResponseModel
from app.models.jurusan import Jurusan
from app.config.db import database
from app.api_models.jurusan_all_models import JurusanResponse

from fastapi.exceptions import HTTPException


class DetailJurusanResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_jurusan': 10,
                    'nama_jurusan': 'Ilmu Komputer',
                    'deskripsi': 'deskripsi jurusan'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def detail_jurusan(id: int):
    check_id_query = Jurusan.select(
        Jurusan.c.id_jurusan).where(Jurusan.c.id_jurusan == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Jurusan tidak ditemukan')

    query = Jurusan.select().where(Jurusan.c.id_jurusan == id)
    jurusan = await database.fetch_one(query)

    return DetailJurusanResponse(
        data=JurusanResponse(
            id_jurusan=jurusan.id_jurusan,
            nama_jurusan=jurusan.nama_jurusan,
            deskripsi=jurusan.deskripsi
        )
    )
