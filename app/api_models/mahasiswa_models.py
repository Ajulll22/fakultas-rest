from pydantic import BaseModel


class MahasiswaResponse(BaseModel):
    id_mahasiswa: int
    npm_mahasiswa: str
    nama_mahasiswa: str
    nama_jurusan: str
