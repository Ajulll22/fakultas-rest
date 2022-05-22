from app.api_models import BaseResponseModel
from app.config.db import database
from app.models.jurusan import Jurusan

from pydantic import BaseModel


class InsertJurusanRequest(BaseModel):
    nama_jurusan: str
    deskripsi: str


class InsertJurusanResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_jurusan': 20,
                    'url': '/v1/jurusan/20',
                },
                'meta': {},
                'message': 'Jurusan Berhasil Ditambahkan',
                'success': True,
                'code': 201
            }
        }


async def insert_jurusan(data: InsertJurusanRequest):
    query = Jurusan.insert().values(nama_jurusan=data.nama_jurusan,
                                    deskripsi=data.deskripsi)
    id_jurusan = await database.execute(query)

    return InsertJurusanResponse(
        data={
            'id_jurusan': id_jurusan,
            'url': f'/v1/jurusan/{id_jurusan}'
        }
    )
