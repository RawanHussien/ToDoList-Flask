from app import app, db
import os

with app.app_context():
    db.create_all()
    print("Database created successfully!")
    print("Database path:", os.path.abspath("test.db"))
