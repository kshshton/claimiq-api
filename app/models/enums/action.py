from enum import Enum


class Action(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMMENTED = "commented"
