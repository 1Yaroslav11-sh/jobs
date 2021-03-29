from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Добавляем капитана
def main():
    db_session.global_init("db/mars_explorer1.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Golad"
    user.name = "Sorti"
    user.age = 20
    user.position = "chief scientist"
    user.speciality = "inventor"
    user.address = "module_1"
    user.email = "Goal_Sort@mars.org"
    user.hashed_password = "inv"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Moonen"
    user.name = "Loon"
    user.age = 31
    user.position = "middle scientist"
    user.speciality = "logistiacan"
    user.address = "module_2"
    user.email = "MoonLoon@mars.org"
    user.hashed_password = "log"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Kaparito"
    user.name = "Venik"
    user.age = 17
    user.position = "pilot"
    user.speciality = "pilot, navigator"
    user.address = "module_2"
    user.email = "kapVen@mars.org"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Back"
    user.name = "Langden"
    user.age = 18
    user.position = "cartographer"
    user.speciality = "cartographer"
    user.address = "module_2"
    user.email = "LangBack@mars.org"
    user.hashed_password = "map"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Benaten"
    user.name = "Ten"
    user.age = 43
    user.position = "chief engineer"
    user.speciality = "builder"
    user.address = "module_1"
    user.email = "benten@mars.org"
    user.hashed_password = "build"

    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
