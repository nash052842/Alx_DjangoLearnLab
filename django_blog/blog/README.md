## Blog Post Management

- List posts at `/posts/` (public)
- View post detail at `/posts/<id>/` (public)
- Create new posts at `/posts/new/` (login required)
- Edit posts at `/posts/<id>/edit/` (author only)
- Delete posts at `/posts/<id>/delete/` (author only)

Permissions enforced with Django mixins for security.
