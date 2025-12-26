from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from .config import settings
from enum import Enum
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseType(Enum):
    """Database type enum for multi-database architecture"""
    CLIENTS = "clients"
    SAMPLES = "samples"
    USERS = "users"
    ORDERS = "orders"
    MERCHANDISER = "merchandiser"


# Connection pool settings (optimized for multi-database setup)
# Reduced per-database pool size since we have 5 databases
POOL_SETTINGS = {
    "pool_pre_ping": True,
    "pool_size": 25,
    "max_overflow": 25,
    "pool_recycle": 1800,
    "pool_timeout": 60,
    "echo_pool": False,
    "pool_use_lifo": True,
}

# Create engines for each database
engines = {
    DatabaseType.CLIENTS: create_engine(settings.DATABASE_URL_CLIENTS, **POOL_SETTINGS),
    DatabaseType.SAMPLES: create_engine(settings.DATABASE_URL_SAMPLES, **POOL_SETTINGS),
    DatabaseType.USERS: create_engine(settings.DATABASE_URL_USERS, **POOL_SETTINGS),
    DatabaseType.ORDERS: create_engine(settings.DATABASE_URL_ORDERS, **POOL_SETTINGS),
    DatabaseType.MERCHANDISER: create_engine(settings.DATABASE_URL_MERCHANDISER, **POOL_SETTINGS),
}

# Create SessionLocal classes for each database
SessionLocalClients = sessionmaker(autocommit=False, autoflush=False, bind=engines[DatabaseType.CLIENTS])
SessionLocalSamples = sessionmaker(autocommit=False, autoflush=False, bind=engines[DatabaseType.SAMPLES])
SessionLocalUsers = sessionmaker(autocommit=False, autoflush=False, bind=engines[DatabaseType.USERS])
SessionLocalOrders = sessionmaker(autocommit=False, autoflush=False, bind=engines[DatabaseType.ORDERS])
SessionLocalMerchandiser = sessionmaker(autocommit=False, autoflush=False, bind=engines[DatabaseType.MERCHANDISER])

# Create separate Base classes for each database
BaseClients = declarative_base()
BaseSamples = declarative_base()
BaseUsers = declarative_base()
BaseOrders = declarative_base()
BaseMerchandiser = declarative_base()

# Legacy aliases for backward compatibility
engine = engines[DatabaseType.SAMPLES]
SessionLocal = SessionLocalSamples
Base = BaseSamples


def get_db_clients():
    """Get database session for clients DB"""
    db = SessionLocalClients()
    try:
        yield db
    finally:
        db.close()


def get_db_samples():
    """Get database session for samples DB"""
    db = SessionLocalSamples()
    try:
        yield db
    finally:
        db.close()


def get_db_users():
    """Get database session for users DB"""
    db = SessionLocalUsers()
    try:
        yield db
    finally:
        db.close()


def get_db_orders():
    """Get database session for orders DB"""
    db = SessionLocalOrders()
    try:
        yield db
    finally:
        db.close()


def get_db_merchandiser():
    """Get database session for merchandiser DB"""
    db = SessionLocalMerchandiser()
    try:
        yield db
    finally:
        db.close()


def get_db():
    """Legacy dependency - defaults to samples DB for backward compatibility"""
    db = SessionLocalSamples()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize all databases - create all tables"""
    max_retries = 5
    retry_interval = 5

    databases = [
        (DatabaseType.CLIENTS, BaseClients, "Clients"),
        (DatabaseType.SAMPLES, BaseSamples, "Samples"),
        (DatabaseType.USERS, BaseUsers, "Users"),
        (DatabaseType.ORDERS, BaseOrders, "Orders"),
        (DatabaseType.MERCHANDISER, BaseMerchandiser, "Merchandiser"),
    ]

    for db_type, base_class, db_name in databases:
        for attempt in range(max_retries):
            try:
                logger.info(f"Connecting to {db_name} database (attempt {attempt + 1}/{max_retries})...")
                base_class.metadata.create_all(bind=engines[db_type])
                logger.info(f"{db_name} database tables created successfully!")
                break
            except OperationalError as e:
                if attempt < max_retries - 1:
                    logger.warning(f"{db_name} DB connection failed: {e}. Retrying in {retry_interval}s...")
                    time.sleep(retry_interval)
                else:
                    logger.error(f"Failed to connect to {db_name} database after {max_retries} attempts")
                    raise

    return True
