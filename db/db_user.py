from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase

#db create users
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#db read users
def get_all_users(db: Session):
    return db.query(DbUser).all()

#db get user by id
def get_user(db: Session, id: int):
    #Handle any exceptions
    return db.query(DbUser).filter(DbUser.id == id).first()

#db update user
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    #Handle any exceptions
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

#db delete user
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    #Handle any exceptions
    db.delete(user)
    db.commit()
    return 'ok'