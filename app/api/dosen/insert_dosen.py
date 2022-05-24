from sqlalchemy import insert


from pydantic import BaseModel, EmailStr


class InsertDosenRequest(BaseModel):
    email: EmailStr


async def insert_dosen(data: InsertDosenRequest):
    pass
