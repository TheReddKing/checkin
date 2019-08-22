"""
Runs the backend server
"""

from flask import Flask
from app.app import app

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=app.config['PORT']
    )