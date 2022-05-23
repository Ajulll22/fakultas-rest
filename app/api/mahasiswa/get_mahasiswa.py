from app.api_models import BaseResponseModel
from app.models.mahasiswa import Mahasiswa
from app.models.jurusan import Jurusan
from app.config.db import database
from app.api_models.mahasiswa_models import MahasiswaResponse


class GetMahasiswaResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'id_mahasiswa': 10,
                        'npm_mahasiswa': '127271271',
                        'nama_mahasiswa': 'Jung Ilhoon',
                        'nama_jurusan': 'Ilmu Komputer'
                    },
                    {
                        'id_mahasiswa': 20,
                        'npm_mahasiswa': '126571271',
                        'nama_mahasiswa': 'Irun',
                        'nama_jurusan': 'Ilmu Komputer'
                    }
                ],
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def get_mahasiswa():
    query = Mahasiswa.select().join(Jurusan).add_columns(Jurusan.c.nama_jurusan)
    mahasiswa_list = await database.fetch_all(query)
    result = []

    for mahasiswa in mahasiswa_list:
        result.append(
            MahasiswaResponse(
                id_mahasiswa=mahasiswa.id_mahasiswa,
                npm_mahasiswa=mahasiswa.npm_mahasiswa,
                nama_mahasiswa=mahasiswa.nama_mahasiswa,
                nama_jurusan=mahasiswa.nama_jurusan
            )
        )

    return GetMahasiswaResponse(
        data=result
    )
