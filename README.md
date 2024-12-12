# Lead Management API

## Overview

This is a robust FastAPI-based application for managing leads using Smartlead API and Supabase as the backend database. The application provides seamless lead creation, campaign management, and performance tracking.

## Features

- FastAPI backend
- Smartlead API integration
- Supabase database management
- Lead creation and tracking
- Campaign performance analytics
- Webhook support for lead status updates

## Prerequisites

- Python 3.9+
- pip
- Supabase account
- Smartlead API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/otabek-olimjonov/smartlead_using_fastapi_supabase_smartlead.ai.git
cd lead-management-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
SMARTLEAD_API_KEY=your_smartlead_api_key
SMARTLEAD_BASE_URL=https://api.smartlead.ai/v1
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key
DEBUG=True
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Campaigns
- `POST /api/v1/campaigns`: Create a new campaign
- Parameters: Campaign details

### Leads
- `POST /api/v1/leads`: Add leads to a campaign
- Parameters: Campaign ID, Lead information

## Supabase Database Setup

1. Create a `leads` table with the following schema:
```sql
CREATE TABLE leads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    phone TEXT,
    campaign_id TEXT,
    smartlead_id TEXT,
    status TEXT DEFAULT 'new',
    additional_fields JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ
);
```

## Configuration

Modify `app/config.py` to adjust application settings.

## Error Handling

The application includes comprehensive error handling:
- Custom exceptions for Smartlead and Supabase errors
- Logging for tracking and debugging
- Consistent error response format

## Security

- Uses environment variables for sensitive information
- Pydantic models for input validation
- Async programming for improved performance

## Webhooks

Supports Smartlead webhook callbacks for:
- Lead status updates
- Real-time lead tracking

## Performance Analytics

Built-in analytics service provides:
- Total leads count
- Leads in last 30 days
- Status distribution
- Conversion rate calculation

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgements

- FastAPI
- Supabase
- Smartlead API