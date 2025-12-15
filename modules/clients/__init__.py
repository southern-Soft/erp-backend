"""Clients module - Buyers, Suppliers, Contacts management"""
from .routes.buyers import router as buyers_router
from .routes.suppliers import router as suppliers_router
from .routes.contacts import router as contacts_router
from .models.client import Buyer, Supplier, ContactPerson, ShippingInfo, BankingInfo
