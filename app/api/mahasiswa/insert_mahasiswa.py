from app.api_models import BaseResponseModel
from app.config.db import database
from app.models.mahasiswa import Mahasiswa
from app.models.jurusan import Jurusan

from pydantic import BaseModel
from fastapi.exceptions import HTTPException


class InsertMahasiswaRequest(BaseModel):
    npm_mahasiswa: str
    nama_mahasiswa: str
    id_jurusan: int


class InsertMahasiswaResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_mahasiswa': 20,
                    'url': '/v1/mahasiswa/20'
                },
                'meta': {},
                'message': 'Mahasiswa Berhasil Ditambahkan',
                'success': True,
                'code': 201
            }
        }


async def insert_mahasiswa(data: InsertMahasiswaRequest):
    npm_unique = Mahasiswa.select(Mahasiswa.c.npm_mahasiswa).where(
        Mahasiswa.c.npm_mahasiswa == data.npm_mahasiswa)
    check_npm = await database.fetch_one(npm_unique)

    if check_npm:
        raise HTTPException(status_code=404, detail='NPM sudah ada')

    jurusan_fk = Jurusan.select(Jurusan.c.id_jurusan).where(
        Jurusan.c.id_jurusan == data.id_jurusan)
    check_jurusan = await database.fetch_one(jurusan_fk)

    if not check_jurusan:
        raise HTTPException(status_code=404, detail='Jurusan tidak ada')

    query = Mahasiswa.insert().values(npm_mahasiswa=data.npm_mahasiswa,
                                      nama_mahasiswa=data.nama_mahasiswa,
                                      id_jurusan=data.id_jurusan)
    id_mahasiswa = await database.execute(query)

    return InsertMahasiswaResponse(
        data={
            'id_mahasiswa': id_mahasiswa,
            'url': f'/v1/mahasiswa/{id_mahasiswa}'
        },
        code=201
    )
