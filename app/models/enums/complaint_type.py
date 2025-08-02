from enum import Enum


class ComplaintType(str, Enum):
    LOGISTICS = "logistics"
    QUALITY = "quality"
    CUSTOMER_SERVICE = "customer_service"
    SAFETY = "safety"
