from sqladmin import ModelView
from sqladmin.fields import SelectField

# Models
from src.database.models.user_model import UserTable
from src.database.models.note_model import NoteTable

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
    category: str = "accounts"

    column_list = [UserTable.id, UserTable.username, UserTable.tg_id]

    # Relation
    form_excluded_columns = [UserTable.notes]

class NoteAdmin(ModelView, model=NoteTable):

    # Permissions
    can_create: bool = True
    can_delete: bool = True
    can_edit: bool = True
    can_export: bool = True
    can_view_details: bool = True

    # Metadata
    name: str = "Сохранялки"
    name_plural: str = "Таблица сохранялки"
    icon: str = "fa fa-book"
    category: str = "user-data"

    column_list: list = [NoteTable.id_user, NoteTable.id, NoteTable.main_text, NoteTable.theme]
    form_create_rules: list = ["main_text", "theme", "id_user", "user"]
    form_edit_rules: list = ["main_text", "theme", "id_user"]

    # Foreign Key
    form_ajax_refs = {
        "user": {
            "fields": ("username", "id"),
            "order_by": ("id")
        }
    }
