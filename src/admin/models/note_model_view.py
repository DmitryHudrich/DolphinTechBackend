from sqladmin import ModelView
from src.database.models.note_model import NoteTable


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
    category: str = "Данные"

    column_list: list = [
        NoteTable.id_user,
        NoteTable.id,
        NoteTable.main_text,
        NoteTable.theme,
    ]
    column_labels: dict = {
        NoteTable.id_user: "Идентификатор пользователя",
        NoteTable.id: "Идентификатор записи",
        NoteTable.main_text: "Основной текст",
        NoteTable.theme: "Тема текста",
    }

    form_create_rules: list = ["main_text", "theme", "id_user", "user"]
    form_edit_rules: list = ["main_text", "theme", "id_user"]

    # Foreign Key
    form_ajax_refs = {"user": {"fields": ("username", "id"), "order_by": ("id")}}
