from core.settings.core_settings import get_settings
from core.settings.user_service_settings import UserSettings
from services.user import AuthUserService, BaseUserService

user_service: BaseUserService | None = None


def set_user_service(service_name: str, services_settings: UserSettings) -> BaseUserService:
    if service_name == "AUTH_USER_SERVICE":
        return AuthUserService(auth_user_settings=services_settings.auth_user_settings)

    elif service_name == "DEBUG_USER_SERVICE":
        if get_settings().app.is_debug:
            from services.user import DebugUserService

            return DebugUserService()
        else:
            raise RuntimeError("Debug service should been used only with is_debug=True")


def get_user_service() -> BaseUserService | None:
    return user_service