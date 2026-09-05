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


# КОМПЛЕКСНОЕ ТЗ: Эндпоинт админки для управления заказами пиццерии НЕ ДОПИСАЛ
# ------------------------------------------------
# Импорты 

from fastapi import FastAPI, Path, HTTPException, Depends
from pydantic import BaseModel, Field, field_validator

from sqlalchemy import select, String, Numeric, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, joinedload, DeclarativeBase, Mapped, mapped_column, relationship

from decimal import Decimal
from datetime import datetime


app = FastAPI()

# ------------------------------------------------
# Инициализация

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/pizza_db"

async_engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,        
    max_overflow=20      
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,    
    class_=AsyncSession,   
    expire_on_commit=False
)

# ------------------------------------------------
# Table model SQL ALCHEMY

class Base(DeclarativeBase):
    pass

class OrderModel(Base):
    __tablename__ = "Order"   


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] 
    pizza_name: Mapped[str]
    price: Mapped[Decimal]
 
# ------------------------------------------------
# Validation model 

class OrderCreateDTO(BaseModel):
    pizza_name: str
    price: int
    ingredients: list[str]

    @field_validator("pizza_name")
    @classmethod
    def check_str(cls, value):
        if value.strip() == '':
            raise ValueError("Название не может быть пустым")
        return value 
    
    @field_validator("ingredients")
    @classmethod
    def check_min_ungridients(cls, value):
        if len(value) < 2:
            raise ValueError("Минимум 2 ингредиента")
        return value 
    

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ------------------------------------------------
# Endpoint

# Админ может сортировать заказы только по трем колонкам: "id", "price", "pizza_name"

@app.get("/admin/orders/")
async def get_admin_orders(sort_by: str = "id" , db: AsyncSession = Depends(get_db)):
    rights = ["id", "price", "pizza_name"]
    if sort_by not in rights:
        raise HTTPException(status_code=400, detail="Неверная колонка для сортировки")
    query = select(OrderModel).order_by(getattr(OrderModel, sort_by))  # getattr(Order, sort_by) что за функция и что она даёт 
    result = await db.execute(query)
    orders = result.scalars().all()
    return orders