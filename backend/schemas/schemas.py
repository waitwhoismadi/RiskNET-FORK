from pydantic import BaseModel

class Position(BaseModel):
    position_id: int
    position_name: str

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    job_title: str

class UserCreate(UserBase):
    position_id: int

class User(UserBase):
    id: int
    position: Position

    class Config:
        orm_mode = True

        
class Reestr_s(BaseModel):
    reestr_id: int
    risk_year: int
    quarter_id: int
    risk_category_id: int
    risk_code_id: str
    owner: str
    control_sp: str
    risk_factor_1: str
    risk_factor_2: str
    risk_factor_3: str
    risk_factor_4: str
    source: str
    swot_id: int
    kri_id:int
    probability: float
    impact: float
    expected_losses: float
    comments: str
    total_probability: float
    total_impact: float
    total_expected_losses: float
    period: str
    priority_id: int
    event_name: str
    event_cost: int
    responsible_sp: str
    effectivity_id: int
    parent_id: int

