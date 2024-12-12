from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID

class LeadBase(BaseModel):
    """
    Base model for lead information
    """
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company: Optional[str] = None
    phone: Optional[str] = None

class LeadCreate(LeadBase):
    """
    Model for creating a new lead
    """
    additional_fields: Optional[Dict[str, Any]] = None
    
    class Config:
        schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "company": "Acme Inc.",
                "phone": "+1234567890",
                "additional_fields": {
                    "source": "website",
                    "campaign": "summer_promo"
                }
            }
        }

class LeadResponse(LeadBase):
    """
    Model for lead response, including database-generated fields
    """
    id: UUID
    campaign_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    smartlead_id: Optional[str] = None
    status: Optional[str] = Field(default="new")