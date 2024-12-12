# models/lead_model.py
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

# utils/error_handling.py
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SmartleadAPIError(Exception):
    """
    Custom exception for Smartlead API related errors
    """
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class SupabaseError(Exception):
    """
    Custom exception for Supabase related errors
    """
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler for the application
    
    :param request: FastAPI request object
    :param exc: Caught exception
    :return: JSON response with error details
    """
    if isinstance(exc, SmartleadAPIError):
        logger.error(f"Smartlead API Error: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "Smartlead API Error",
                "details": exc.message
            }
        )
    
    if isinstance(exc, SupabaseError):
        logger.error(f"Supabase Error: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "Supabase Database Error",
                "details": exc.message
            }
        )
    
    # Catch-all for unexpected errors
    logger.exception("Unexpected error occurred")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc)
        }
    )