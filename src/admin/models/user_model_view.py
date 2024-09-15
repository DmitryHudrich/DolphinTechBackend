from sqladmin import ModelView

# Models
from src.database.models.user_model import UserTable


class UserAdmin(ModelView, model=UserTable):
    # Permissions
    can_create: bool = True
    can_edit: bool = True
    can_delete: bool = True
    can_view_details: bool = True
    can_export: bool = True

    # Metadata
    name: str = "Пользователь"
    name_plural: str = "Таблица пользователей"
    icon: str = "fa-solid fa-user"
    category: str = "Пользователи"

    column_list = [UserTable.id, UserTable.username, UserTable.tg_id]
    column_labels: dict = {
        UserTable.id: "Идентификатор",
        UserTable.username: "Имя пользователя",
        UserTable.tg_id: "Телеграмм идентификатор",
        UserTable.notes: "Заметки",
    }

    # Relation
    form_excluded_columns = [UserTable.notes]
