from app.api_models import BaseResponseModel
from app.models.jurusan import Jurusan
from app.models.mahasiswa import Mahasiswa
from app.config.db import database
from app.api_models.mahasiswa_models import MahasiswaResponse

from fastapi.exceptions import HTTPException


class DetailMahasiswaResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id_mahasiswa': 10,
                    'npm_mahasiswa': '1817051042',
                    'nama_mahasiswa': 'Jung Ilhoon',
                    'nama_jurusan': 'Ilmu Komputer',
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def detail_mahasiswa(id: int):
    check_id_query = Mahasiswa.select(
        Mahasiswa.c.id_mahasiswa).where(Mahasiswa.c.id_mahasiswa == id)
    check_id = await database.fetch_one(check_id_query)

    if not check_id:
        raise HTTPException(404, detail='Mahasiswa tidak ditemukan')

    query = Mahasiswa.select().join(Jurusan).add_columns(
        Jurusan.c.nama_jurusan).where(Mahasiswa.c.id_mahasiswa == id)
    mahasiswa = await database.fetch_one(query)

    return DetailMahasiswaResponse(
        data=MahasiswaResponse(
            id_mahasiswa=mahasiswa.id_mahasiswa,
            npm_mahasiswa=mahasiswa.npm_mahasiswa,
            nama_mahasiswa=mahasiswa.nama_mahasiswa,
            nama_jurusan=mahasiswa.nama_jurusan
        )
    )
