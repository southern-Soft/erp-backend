from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


# ==================== UoM Category ====================

class UoMCategoryBase(BaseModel):
    uom_category: str
    uom_id: Optional[str] = None
    uom_name: str
    uom_description: Optional[str] = None
    is_active: Optional[bool] = True


class UoMCategoryCreate(UoMCategoryBase):
    pass


class UoMCategoryUpdate(BaseModel):
    uom_category: Optional[str] = None
    uom_id: Optional[str] = None
    uom_name: Optional[str] = None
    uom_description: Optional[str] = None
    is_active: Optional[bool] = None


class UoMCategoryResponse(UoMCategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== UoM ====================

class UoMBase(BaseModel):
    category_id: int
    name: str
    symbol: str
    factor: Optional[Decimal] = Decimal("1.0")
    is_base: Optional[bool] = False
    is_active: Optional[bool] = True
    remarks: Optional[str] = None


class UoMCreate(UoMBase):
    pass


class UoMUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    factor: Optional[Decimal] = None
    is_base: Optional[bool] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class UoMResponse(UoMBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Color Family ====================

class ColorFamilyBase(BaseModel):
    color_family: str
    color_family_code: Optional[str] = None
    color_family_code_type: Optional[str] = None
    sort_order: Optional[int] = 0
    is_active: Optional[bool] = True


class ColorFamilyCreate(ColorFamilyBase):
    pass


class ColorFamilyUpdate(BaseModel):
    color_family: Optional[str] = None
    color_family_code: Optional[str] = None
    color_family_code_type: Optional[str] = None
    sort_order: Optional[int] = None
    is_active: Optional[bool] = None


class ColorFamilyResponse(ColorFamilyBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Color ====================

class ColorBase(BaseModel):
    color: str
    color_family_id: int
    color_code: Optional[str] = None
    color_code_type: Optional[str] = None
    is_active: Optional[bool] = True


class ColorCreate(ColorBase):
    pass


class ColorUpdate(BaseModel):
    color: Optional[str] = None
    color_family_id: Optional[int] = None
    color_code: Optional[str] = None
    color_code_type: Optional[str] = None
    is_active: Optional[bool] = None


class ColorResponse(ColorBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Color Value ====================

class ColorValueBase(BaseModel):
    color_value_code: str
    color_value_code_type: str
    sort_order: Optional[int] = 0
    is_active: Optional[bool] = True


class ColorValueCreate(ColorValueBase):
    pass


class ColorValueUpdate(BaseModel):
    color_value_code: Optional[str] = None
    color_value_code_type: Optional[str] = None
    sort_order: Optional[int] = None
    is_active: Optional[bool] = None


class ColorValueResponse(ColorValueBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Color Master ====================

class ColorMasterBase(BaseModel):
    color_id: int
    color_family_id: int
    color_value_id: Optional[int] = None
    color_name: str
    color_code_type: Optional[str] = None
    color_code: Optional[str] = None
    hex_value: Optional[str] = None
    is_active: Optional[bool] = True
    remarks: Optional[str] = None


class ColorMasterCreate(ColorMasterBase):
    pass


class ColorMasterUpdate(BaseModel):
    color_id: Optional[int] = None
    color_family_id: Optional[int] = None
    color_value_id: Optional[int] = None
    color_name: Optional[str] = None
    color_code_type: Optional[str] = None
    color_code: Optional[str] = None
    hex_value: Optional[str] = None
    is_active: Optional[bool] = None
    remarks: Optional[str] = None


class ColorMasterResponse(ColorMasterBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Country ====================

class CountryBase(BaseModel):
    country_id: str
    country_name: str
    international_country_code: Optional[str] = None
    international_dialing_number: Optional[str] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = True


class CountryCreate(CountryBase):
    pass


class CountryUpdate(BaseModel):
    country_id: Optional[str] = None
    country_name: Optional[str] = None
    international_country_code: Optional[str] = None
    international_dialing_number: Optional[str] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None


class CountryResponse(CountryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== City ====================

class CityBase(BaseModel):
    city_id: str
    city_name: str
    country_id: int
    state_province: Optional[str] = None
    is_active: Optional[bool] = True


class CityCreate(CityBase):
    pass


class CityUpdate(BaseModel):
    city_id: Optional[str] = None
    city_name: Optional[str] = None
    country_id: Optional[int] = None
    state_province: Optional[str] = None
    is_active: Optional[bool] = None


class CityResponse(CityBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ==================== Port ====================

class PortBase(BaseModel):
    country_id: int
    city_id: Optional[int] = None
    locode: str
    port_name: str
    name_wo_diacritics: Optional[str] = None
    subdivision: Optional[str] = None
    function: Optional[str] = None
    status: Optional[str] = None
    date: Optional[str] = None
    iata: Optional[str] = None
    coordinates: Optional[str] = None
    remarks: Optional[str] = None
    is_active: Optional[bool] = True


class PortCreate(PortBase):
    pass


class PortUpdate(BaseModel):
    country_id: Optional[int] = None
    city_id: Optional[int] = None
    locode: Optional[str] = None
    port_name: Optional[str] = None
    name_wo_diacritics: Optional[str] = None
    subdivision: Optional[str] = None
    function: Optional[str] = None
    status: Optional[str] = None
    date: Optional[str] = None
    iata: Optional[str] = None
    coordinates: Optional[str] = None
    remarks: Optional[str] = None
    is_active: Optional[bool] = None


class PortResponse(PortBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
