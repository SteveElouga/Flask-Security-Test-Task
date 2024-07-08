from .extensions import db, app
from werkzeug.security import generate_password_hash, check_password_hash

import logging as lg

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer(), primary_key = True)
    first_name = db.Column(db.String(), nullable = False)
    last_name = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.Text())
    
    def __repr__(self) -> str:
        return f"<User {self.email}>"
    
    def set_password(self, password):
        self.password = generate_password_hash(password=password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email = email).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete()
        db.session.commit()
        
 
@app.cli.command()  
def init_db():
    # db.drop_all()
    db.create_all()
    lg.warning('Database initialized!')