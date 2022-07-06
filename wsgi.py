
# app.py
from flask_migrate import Migrate
from app import app,db
import route



migrate = Migrate(app, db)



if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)