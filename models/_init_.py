#!/usr/bin/python3
"""creates a static FileStorage instance"""

from .engine.file_storage import FileStorage
storage = FileStorage()
# storage._FileStorage__file_path = 'data.json'
# storage._FileStorage__objects = {}
storage.reload()
