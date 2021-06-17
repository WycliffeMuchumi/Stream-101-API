from app.api.users.models.users import User
from app import db
from faker import Faker

"""
    Instantiating our Faker class from faker library.
    Faker is used to generate fake data.Fake data is often used 
    for testing or filling databases with some dummy data.Faker is heavily
    inspired by PHP's Faker, Perl's Data::Faker, and by Ruby's Faker.
"""
fake = Faker()


def fake_data(number_of_records):
    for i in range(0, number_of_records):
        fullName = fake.name()
        firstName, lastName = fullName.split(" ", 1)
        userName = fake.name()
        email = fake.email()
        password = fake.password()

        fake_user = User(firstName=firstName, lastName=lastName, userName=userName,
                    email=email, phoneNumber='', password=password)
        db.session.add(fake_user)
        db.session.commit()



        



