# Security Measures in Django App

## ✅ Settings Configured
- `DEBUG = False` for production
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Blocks content-type sniffing
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Cookies sent only over HTTPS
- `SECURE_SSL_REDIRECT = True`: Forces HTTPS connections

## ✅ CSRF Protection
All forms include `{% csrf_token %}`.
CSRF middleware is enabled by default.

## ✅ SQL Injection Protection
- All views use Django ORM.
- No raw SQL.
- Forms and cleaned input used for user-submitted data.

## ✅ Content Security Policy
- Implemented using `django-csp`.
- Restricts JS, CSS, and fonts to known domains to prevent XSS.

## ✅ Manual Testing Checklist
- Tested access over HTTP: confirmed HTTPS redirection.
- Submitted forms without CSRF token: request blocked.
- Tried XSS via `<script>` input in forms: input was sanitized and/or escaped.
- Attempted SQL injection (`'; DROP TABLE ...`): query safely filtered by ORM.

