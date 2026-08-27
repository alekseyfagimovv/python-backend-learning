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



# Эндпоинт для перевода сотрудника между отделами внутри CRM-системы.
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()

class OneElement(BaseModel):
    new_department : str = Field(min_length=3, max_length=50)
    reason: str = Field(default=None)

@app.post("/api/v1/employees/{employee_id}/transfer")
async def read_root(dto: OneElement,
                    employee_id: Annotated[int, Path(title="ID сотрудника", gt=0)],
                    is_urgent: bool = False):
    return {"employee_id": employee_id,
            "new_department": dto.new_department,
            "reason": dto.reason,
            "is_urgent": is_urgent}


