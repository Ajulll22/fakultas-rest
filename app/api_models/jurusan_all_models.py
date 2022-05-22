from pydantic import BaseModel


class JurusanResponse(BaseModel):
    id_jurusan: int
    nama_jurusan: str
    deskripsi: str
