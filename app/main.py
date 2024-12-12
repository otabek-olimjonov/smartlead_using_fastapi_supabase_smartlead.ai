from fastapi import FastAPI
from app.routes import lead_routes
from app.config import settings

app = FastAPI(
    title="Lead Management API",
    description="API for managing leads with Smartlead and Supabase integration",
    debug=settings.DEBUG
)

# Include routers
app.include_router(lead_routes.router, prefix="/api/v1")