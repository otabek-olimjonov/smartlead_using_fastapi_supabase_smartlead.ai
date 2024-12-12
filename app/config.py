import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Smartlead API Configuration
    SMARTLEAD_API_KEY = os.getenv('SMARTLEAD_API_KEY')
    SMARTLEAD_BASE_URL = os.getenv('SMARTLEAD_BASE_URL', 'https://api.smartlead.ai/v1')
    
    # Supabase Configuration
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # Application Settings
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    
settings = Settings()