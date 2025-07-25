# Permissions and Groups Setup (bookshelf app)

This app uses Django's group and permission system to restrict access to Book views.

## Custom Permissions
Defined in `Book` model:
- `can_view`: View book list
- `can_create`: Add new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

## User Groups
Set up via admin or `setup_groups` command:

- **Viewers**
  - can_view

- **Editors**
  - can_view, can_create, can_edit

- **Admins**
  - All permissions

## Views
- `book_list` – requires `can_view`
- `book_create` – requires `can_create`
- `book_edit` – requires `can_edit`
- `book_delete` – requires `can_delete`

## How to Setup (Dev)
1. Run `python manage.py setup_groups`
2. Assign users to groups via Django admin
