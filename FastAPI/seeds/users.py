from sqlmodel import Session
from app.models import User  # Assuming you have a User model defined
from app.database_connection import engine
from faker import Faker

fake = Faker()

def create_initial_data():
    # Creating an instance of the User model
    # loop 10 times creating a new user each time
    users = []

    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.email(),
            age=fake.random_int(min=18, max=99),
            password=fake.password(length=12)
        )
        users.append(user)
    
    # Open a session to insert the data
    with Session(engine) as session:
        session.add_all(users)  # Add multiple records to the session
        session.commit()  # Commit the transaction to the database

    print("Database seeded successfully!")

# You can run this function directly to seed the database
if __name__ == "__main__":
    create_initial_data()
