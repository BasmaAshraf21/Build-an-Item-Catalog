import sys
import os



from sqlalchemy import Column, Integer, String, ForeignKey, Table

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, relationship 

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Restaurant(Base):
    __tablename__= 'restaurant'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }
   


class MenuItem(Base):
    __tablename__= 'menu_item'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship("Restaurant")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
  
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }









######insert at end of file######
if __name__ == '__main__':
    engine = create_engine(
        'sqlite:///restaurantmenuwithusers.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind = engine)
    session = DBSession()


    # Create dummy user
    User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
                 picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
    session.add(User1)
    session.commit()

    
    #create pizzahut restaurant
    pizzahut = Restaurant(user_id='1', name='Pizza Hut')
    session.add(pizzahut)
    session.commit()
    
    # Menu for pizzahut
    supersupreme = MenuItem(user_id='1',name = 'SUPER SUPREME',
                           description= "Our famous combination of Beef Pepperoni, juicy Beef, Mushrooms, Green Peppers, Onions, Black Olives and melting mozzarella cheese.",
                           price = "$32",course= "entree", restaurant_id = "1")
    session.add(supersupreme)
    session.commit()

    margherita = MenuItem(user_id='1',name = 'MARGHERITA',
                           description= "Go Back to where it all began with the classic cheese and tomato base",
                           price = "$3.4",course= "entree", restaurant_id = "1")
    session.add(margherita)
    session.commit()

    chickensupreme = MenuItem(user_id='1',name = 'CHICKEN SUPREME',
                           description= "The ultimate mix of Chicken together with Mushrooms, Red Onions, Green Peppers, fresh Tomatoes, Olives and melting mozzarella cheese.",
                           price = "$49",course= "entree", restaurant_id = "1")
    session.add(chickensupreme)
    session.commit()

    #create pizzahut restaurant
    pizzaking = Restaurant(user_id='1',name='Pizza King')
    session.add(pizzaking)
    session.commit()

    # Menu for pizzaking
    vegetarianpizza = MenuItem(user_id='1',name = 'Vegetarian Pizza - Italian',
                           description= "Tomatoes, green pepper, onion, mushroom, mozzarella cheese and black olive",
                           price = "$91",course= "entree", restaurant_id = "2")
    session.add(vegetarianpizza)
    session.commit()

    cheeseloverspizza = MenuItem(user_id='1',name = 'Cheese Lovers Pizza - Pan',
                           description= "Mozzarella cheese, cheddar cheese, Gouda cheese, tomato sauce, served with 2 toppings",
                           price = "$22",course= "entree", restaurant_id = "2")
    session.add(cheeseloverspizza)
    session.commit()

    margaritapizza = MenuItem(user_id='1',name = 'Margarita Pizza - Italian',
                           description= "Mozzarella cheese and tomato sauce",
                           price = "$33",course= "entree", restaurant_id = "2")
    session.add(margaritapizza)
    session.commit()

    #create KFC restaurant
    kfc = Restaurant(user_id='1',name='KFC')
    session.add(kfc)
    session.commit()

    # Menu for KFC
    spicycolonel = MenuItem(user_id='1',name = 'SPICY COLONELS ORIGINAL',
                           description= "Enjoy comfort food that comes with a kick. The Spicy Colonels Original is loaded with flavour.",
                           price = "$42",course= "entree", restaurant_id = "3")
    session.add(spicycolonel)
    session.commit()


    vegetarianpizza = MenuItem(user_id='1',name = 'Vegetarian Pizza - Italian',
                           description= "Tomatoes, green pepper, onion, mushroom, mozzarella cheese and black olive",
                           price = "$32",course= "entree", restaurant_id = "3")
    session.add(vegetarianpizza)
    session.commit()

    bigcrunch = MenuItem(user_id='1',name = 'BIG CRUNCH',
                           description= "Welcome your family to the dinner table with the Big Crunch.",
                           price = "$88",course= "entree", restaurant_id = "3")
    session.add(bigcrunch)
    session.commit()

    twister = MenuItem(user_id='1',name = 'TWISTER',
                           description= "The taste you love, all wrapped up and toasted to seal in the flavour.",
                           price = "$77",course= "entree", restaurant_id = "3")
    session.add(twister)
    session.commit()

    #create macdonalds restaurant
    macdonalds = Restaurant(user_id='1',name='Macdonalds')
    session.add(macdonalds)
    session.commit()

    # Menu for macdonalds    
    fansmeal = MenuItem(user_id='1',name = 'Fans Meal',
                           description= "2 Chicken Filet sandwiches (Regular or Spicy or Mix) + 2 Regular Fries + 1 Liter Coke bottle + 9 Pcs Chicken McNuggets + 2 World Cup Coke Gift Bottles.",
                           price = "$66",course= "entree", restaurant_id = "4")
    session.add(fansmeal)
    session.commit()


    bigtasty = MenuItem(user_id='1',name = 'Big Tasty',
                           description= "It is the juicy beef patty smothered in three extraordinary slices of Emmental cheese, and topped with sliced tomato, shredded lettuce, onions and that special Big Tasty sauce.",
                           price = "$55",course= "entree", restaurant_id = "4")
    session.add(bigtasty)
    session.commit()


    cheeseburger = MenuItem(user_id='1',name = 'Cheeseburger',
                           description= "Welcome your family to the dinner table with the Big Crunch.",
                           price = "$42",course= "entree", restaurant_id = "4")
    session.add(cheeseburger)
    session.commit()

    hardees = Restaurant(user_id='1',name='Hardees')
    session.add(hardees)
    session.commit()





    

    


    
