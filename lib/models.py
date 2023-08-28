from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///db/beangrade.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    @classmethod
    def find_by_name(cls, name):
        user = session.query(cls).get(name)
        if user:
            return user
        else:
            return "No user found!"

    @classmethod
    def add_new_user(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        print(f"User {name} created.")

    def __repr__(self):
        return f"User #{self.id}: " + f"{self.name}"


class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer(), primary_key=True)
    roaster = Column(String(), index=True)
    name = Column(String())
    roast_level = Column(String(), index=True)

    @classmethod
    def get_new_coffee(self):
        pass

    def __repr__(self):
        return (
            f"Coffee #{self.id}: "
            + f"{self.roaster} {self.name}, "
            + f"a {self.roast_level} roast"
        )


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    coffee_id = Column(Integer(), ForeignKey("coffees.id"))
    rating = Column(Integer(), index=True)

    user = relationship("User", backref=backref("User"))
    coffee = relationship("Coffee", backref=backref("Coffee"))

    def __repr__(self):
        return (
            f"\nRating\n"
            + f"id = {self.id}\n"
            + f"user_id = {self.user_id}\n"
            + f"user_name = {self.user.name}\n"
            + f"coffee_id = {self.coffee_id}\n"
            + f"coffee_roaster = {self.coffee.roaster}\n"
            + f"coffee_roaster = {self.coffee.name}\n"
            + f"rating = {self.rating}\n"
        )
