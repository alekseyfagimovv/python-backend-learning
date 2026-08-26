# Дефолтная модель валидатора пидантик
from pydantic import BaseModel, Field, field_validator


class BookingCreate(BaseModel):
    hotel_name: str
    guests_count: int = Field(ge=1, le=4) 
    room_type: str

    @field_validator("room_type")
    @classmethod
    def check_size(cls, value: str) -> str:
        if value != value.upper():
            raise ValueError("Все буквы должны быть большими")
        return value



# Схема валидации со сроком аренды и post эдпоинтом
from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator

app = FastAPI()

class RentEquipmentDTO(BaseModel):
    tool_name: str
    days: int = Field(ge=1, le=30) 
    
    @model_validator(mode="after")
    def check_perforator(self) -> "RentEquipmentDTO":
        if self.tool_name.lower() == "промышленный перфоратор" and self.days > 5:
                raise ValueError("Нельзя арендовать больше чем на 5 дней")
        return self
    
@app.post("/rent/{contract_number}")
async def read_root(rent_info: RentEquipmentDTO, 
                    contract_number: int, 
                    manager_name: str = "System"):
    return {"contract_number": contract_number,
            "manager_name": manager_name,
            "rent_info": rent_info.model_dump()}