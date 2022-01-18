from enum import Enum
from uuid import UUID

from pydantic import BaseModel

from core.settings.core_settings import get_settings


class DeliveryType(str, Enum):
    "Delivery types variants"
    sms = "sms"
    email = "email"
    if get_settings().app.is_debug:
        debug = "debug"


class Event(BaseModel):
    "Event for sending notification"
    user_id: UUID
    delivery_type: DeliveryType
    event_type: str | None
    template_id: str | None
