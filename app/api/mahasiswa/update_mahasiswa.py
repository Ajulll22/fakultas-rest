from app.api_models import BaseResponseModel
from app.config.db import database
from app.models.jurusan import Jurusan
from app.models.mahasiswa import Mahasiswa

from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException


class UpdateMahasiswaRequest(BaseModel):
    npm_mahasiswa: Optional[str]
    nama_mahasiswa: Optional[str]
    id_jurusan: Optional[int]


class UpdateMahasiswaResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_mahasiswa': 20,
                    'url': '/v1/mahasiswa/20',
                },
                'meta': {},
                'message': 'Mahasiswa Berhasil Terupdate',
                'success': True,
                'code': 201
            }
        }


async def update_mahasiswa(id: int, data: UpdateMahasiswaRequest):
    check_id_query = Mahasiswa.select(
        Mahasiswa.c.id_mahasiswa).where(Mahasiswa.c.id_mahasiswa == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Mahasiswa tidak ditemukan')
