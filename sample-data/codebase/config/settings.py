"""
Application configuration. Values loaded from environment variables.
"""
import os

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://localhost:5432/portfolio_mgmt")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Market data vendors
BLOOMBERG_HOST = os.getenv("BLOOMBERG_HOST", "localhost")
BLOOMBERG_PORT = int(os.getenv("BLOOMBERG_PORT", "8194"))
REFINITIV_API_KEY = os.getenv("REFINITIV_API_KEY", "")

# Custodian SFTP connections
CUSTODIAN_SFTP = {
    "schwab": {
        "host": os.getenv("SCHWAB_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "positions_*.csv",
        "recon_time": "06:00",  # EST
    },
    "fidelity": {
        "host": os.getenv("FIDELITY_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "FIDELITY_POS_*.dat",
        "recon_time": "07:00",
    },
    "pershing": {
        "host": os.getenv("PERSHING_SFTP_HOST", ""),
        "port": 22,
        "file_pattern": "DTCC_*.xml",
        "recon_time": "06:30",
    },
}

# Drift monitoring
DRIFT_CHECK_INTERVAL_SECONDS = int(os.getenv("DRIFT_CHECK_INTERVAL", "300"))  # 5 min
DRIFT_ALERT_COOLDOWN_MINUTES = int(os.getenv("DRIFT_ALERT_COOLDOWN", "60"))

# Celery task queue
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", REDIS_URL)
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", REDIS_URL)
