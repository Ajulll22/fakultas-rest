from app.api_models import BaseResponseModel
from app.config.db import database
from app.models.jurusan import Jurusan

from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException


class UpdateJurusanRequest(BaseModel):
    nama_jurusan: Optional[str]
    deskripsi: Optional[str]


class UpdateJurusanResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_jurusan': 20,
                    'url': '/v1/jurusan/20',
                },
                'meta': {},
                'message': 'Jurusan Berhasil Terupdate',
                'success': True,
                'code': 201
            }
        }


async def update_jurusan(id: int, data: UpdateJurusanRequest):
    check_id_query = Jurusan.select(
        Jurusan.c.id_jurusan).where(Jurusan.c.id_jurusan == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Jurusan tidak ditemukan')

    jurusan_data = jsonable_encoder(data)

    values_to_update = {}

    if 'nama_jurusan' in jurusan_data and jurusan_data['nama_jurusan']:
        values_to_update.update({
            'nama_jurusan': jurusan_data['nama_jurusan']
        })
    if 'deskripsi' in jurusan_data and jurusan_data['deskripsi']:
        values_to_update.update({
            'deskripsi': jurusan_data['deskripsi']
        })

    if not values_to_update:
        raise HTTPException(400, detail='Data tidak boleh kosong')

    query = Jurusan.update().where(Jurusan.c.id_jurusan ==
                                   id).values(**values_to_update)
    await database.execute(query)

    return UpdateJurusanResponse(
        data={
            'id_jurusan': id,
            'url': f'/v1/jurusan/{id}'
        }
    )
