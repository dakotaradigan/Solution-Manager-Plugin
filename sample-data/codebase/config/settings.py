"""
Application configuration. Values loaded from environment variables.
"""
import os

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://localhost:5432/transition_analysis")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Custodian SFTP connections (for holdings file ingestion)
CUSTODIAN_SFTP = {
    "schwab": {
        "host": os.getenv("SCHWAB_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "positions_*.csv",
        "format": "csv",
    },
    "fidelity": {
        "host": os.getenv("FIDELITY_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "FIDELITY_POS_*.dat",
        "format": "pipe_delimited",
    },
    "pershing": {
        "host": os.getenv("PERSHING_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "DTCC_*.xml",
        "format": "dtcc_xml",
    },
    "bny": {
        "host": os.getenv("BNY_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "BNY_HOLDINGS_*.xml",
        "format": "proprietary_xml",
    },
}

# Security master (for mapping incoming holdings to internal identifiers)
SECURITY_MASTER_API = os.getenv("SECURITY_MASTER_API", "http://localhost:8080/api/v1/securities")
SECURITY_MASTER_CACHE_TTL = int(os.getenv("SECURITY_MASTER_CACHE_TTL", "3600"))

# Market data (for current pricing of holdings)
PRICING_API = os.getenv("PRICING_API", "http://localhost:8081/api/v1/prices")

# Optimization
MAX_OPTIMIZATION_ITERATIONS = int(os.getenv("MAX_OPTIMIZATION_ITERATIONS", "1000"))
TRADEOFF_CURVE_DEFAULT_POINTS = int(os.getenv("TRADEOFF_CURVE_POINTS", "10"))
DEFAULT_MAX_TRACKING_ERROR_BPS = int(os.getenv("DEFAULT_MAX_TRACKING_ERROR_BPS", "200"))

# SLA and routing
DEFAULT_SLA_DAYS_STANDARD = int(os.getenv("SLA_DAYS_STANDARD", "10"))
DEFAULT_SLA_DAYS_HIGH = int(os.getenv("SLA_DAYS_HIGH", "5"))
DEFAULT_SLA_DAYS_STRATEGIC = int(os.getenv("SLA_DAYS_STRATEGIC", "3"))

# Celery task queue
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", REDIS_URL)
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", REDIS_URL)

# Compliance service
COMPLIANCE_API = os.getenv("COMPLIANCE_API", "http://localhost:8082/api/v1/compliance")
