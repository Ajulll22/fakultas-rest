from fastapi import APIRouter

from app.config.db import database
from app.api.jurusan.get_jurusan import get_jurusan, GetJurusanResponse
from app.api.jurusan.insert_jurusan import insert_jurusan, InsertJurusanResponse
from app.api.jurusan.update_jurusan import update_jurusan, UpdateJurusanResponse
from app.api.jurusan.delete_jurusan import delete_jurusan
from app.api.jurusan.detail_jurusan import detail_jurusan, DetailJurusanResponse

from app.api.mahasiswa.get_mahasiswa import get_mahasiswa, GetMahasiswaResponse
from app.api.mahasiswa.insert_mahasiswa import insert_mahasiswa, InsertMahasiswaResponse
from app.api.mahasiswa.update_mahasiswa import update_mahasiswa, UpdateMahasiswaResponse
from app.api.mahasiswa.delete_mahasiswa import delete_mahasiswa


api_router = APIRouter()


@api_router.on_event('startup')
async def startup():
    await database.connect()


@api_router.on_event('shutdown')
async def shutdown():
    await database.disconnect()


api_router.add_api_route('/v1/jurusan', get_jurusan,
                         methods=['GET'], tags=['Jurusan'], response_model=GetJurusanResponse)
api_router.add_api_route('/v1/jurusan', insert_jurusan,
                         methods=['POST'], tags=['Jurusan'], response_model=InsertJurusanResponse, status_code=201)
api_router.add_api_route('/v1/jurusan/{id}', update_jurusan,
                         methods=['PUT'], tags=['Jurusan'], response_model=UpdateJurusanResponse, status_code=201)
api_router.add_api_route('/v1/jurusan/{id}', delete_jurusan,
                         methods=['DELETE'], tags=['Jurusan'], status_code=204)
api_router.add_api_route('/v1/jurusan/{id}', detail_jurusan,
                         methods=['GET'], tags=['Jurusan'], response_model=DetailJurusanResponse)


api_router.add_api_route('/v1/mahasiswa', get_mahasiswa,
                         methods=['GET'], tags=['Mahasiswa'], response_model=GetMahasiswaResponse)
api_router.add_api_route('/v1/mahasiswa', insert_mahasiswa,
                         methods=['POST'], tags=['Mahasiswa'], response_model=InsertMahasiswaResponse, status_code=201)
api_router.add_api_route('/v1/mahasiswa/{id}', update_mahasiswa,
                         methods=['PUT'], tags=['Mahasiswa'], response_model=UpdateMahasiswaResponse, status_code=201)
api_router.add_api_route('/v1/mahasiswa/{id}', delete_mahasiswa,
                         methods=['DELETE'], tags=['Mahasiswa'], status_code=204)
