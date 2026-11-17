"""
Network Security Utilities for Student Support Management System
Provides input sanitization, CSRF protection helpers, secure token generation,
and HTTP security headers for safeguarding the web application.
"""

import html
import re
import secrets
from functools import wraps
from flask import request, abort, make_response

def sanitize_input(text):
    """
    Sanitizes user input to prevent Cross-Site Scripting (XSS) attacks
    by escaping special HTML characters.
    """
    if not text:
        return ""
    return html.escape(str(text).strip())


def validate_student_id(student_id):
    """
    Validates student ID format to ensure it conforms to expected patterns
    (e.g., alphanumeric strings between 3 and 20 characters).
    """
    pattern = r"^[A-Za-z0-9]{3,20}$"
    return bool(re.match(pattern, str(student_id)))


def generate_secure_token(length=32):
    """
    Generates a cryptographically strong random token for session management
    or secure CSRF validation.
    """
    return secrets.token_hex(length)


def add_security_headers(response):
    """
    Flask after_request handler to inject standard security headers
    into outgoing HTTP responses.
    """
    # Prevent MIME-type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Prevent clickjacking attacks by disallowing framing
    response.headers['X-Frame-Options'] = 'DENY'
    
    # Enable browser XSS filtering
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Content Security Policy (CSP)
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    
    return response


def secure_required(f):
    """
    Decorator to ensure requests originate over HTTPS in production environments.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if request is secure or running locally
        if not request.is_secure and request.host.startswith('localhost') is False:
            # Redirect HTTP to HTTPS
            if request.url.startswith('http://'):
                secure_url = request.url.replace('http://', 'https://', 1)
                return make_response('', 301, {'Location': secure_url})
        return f(*args, **kwargs)
    return decorated_function