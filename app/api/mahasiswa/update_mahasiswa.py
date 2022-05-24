from operator import and_
from app.api_models import BaseResponseModel
from app.config.db import database
from app.models.jurusan import Jurusan
from app.models.mahasiswa import Mahasiswa

from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy import and_


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
    mahasiswa_data = jsonable_encoder(data)

    check_id_query = Mahasiswa.select(
        Mahasiswa.c.id_mahasiswa).where(Mahasiswa.c.id_mahasiswa == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Mahasiswa tidak ditemukan')

    values_to_update = {}

    if 'npm_mahasiswa' in mahasiswa_data and mahasiswa_data['npm_mahasiswa']:
        # check username exist
        check_npm_query = Mahasiswa.select().where(and_(
            Mahasiswa.c.npm_mahasiswa == mahasiswa_data['npm_mahasiswa'],
            Mahasiswa.c.id_mahasiswa != id))
        check_npm = await database.fetch_one(check_npm_query)

        if check_npm:
            raise HTTPException(400, 'NPM Sudah Ada')

        values_to_update.update({
            'npm_mahasiswa': mahasiswa_data['npm_mahasiswa']
        })
    if 'nama_mahasiswa' in mahasiswa_data and mahasiswa_data['nama_mahasiswa']:
        values_to_update.update({
            'nama_mahasiswa': mahasiswa_data['nama_mahasiswa']
        })
    if 'id_jurusan' in mahasiswa_data and mahasiswa_data['id_jurusan']:
        values_to_update.update({
            'id_jurusan': mahasiswa_data['id_jurusan']
        })

    query = Mahasiswa.update().where(Mahasiswa.c.id_mahasiswa ==
                                     id).values(**values_to_update)
    await database.execute(query)

    return UpdateMahasiswaResponse(
        data={
            'id_mahasiswa': id,
            'url': f'/v1/mahasiswa/{id}'
        }
    )
