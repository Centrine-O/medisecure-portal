from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.api import auth
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="MediSecure Portal API",
    description="Secure Healthcare Patient Portal with HIPAA-compliant data handling",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

# CORS middleware - allows frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=    
    
    
    settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
@app.on_event("startup")
def startup_event():
    """
    Create all database tables on startup.
    In production, use Alembic migrations instead.
    """
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully!")

# Include routers
app.include_router(auth.router, prefix="/api/v1")

# Health check endpoint
@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
def root():
    """
    API root endpoint.
    """
    return {
        "message": "Welcome to MediSecure Portal API",
        "docs": "/docs",
        "health": "/health"
    }