from app.api_models import BaseResponseModel
from app.api_models.jurusan_all_models import JurusanResponse
from app.config.db import database
from app.models.jurusan import Jurusan


class GetJurusanResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'id_jurusan': 10,
                        'nama_jurusan': 'Ilmu Komputer',
                        'deskripsi': 'deskripsi jurusan'
                    },
                    {
                        'id_jurusan': 20,
                        'nama_jurusan': 'Biologi',
                        'deskripsi': 'deskripsi jurusan'
                    },
                ],
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def get_jurusan():
    query = Jurusan.select()
    jurusan_list = await database.fetch_all(query)
    result = []

    for jurusan in jurusan_list:
        result.append(
            JurusanResponse(
                id_jurusan=jurusan.id_jurusan,
                nama_jurusan=jurusan.nama_jurusan,
                deskripsi=jurusan.deskripsi
            )
        )

    return GetJurusanResponse(
        data=result
    )
