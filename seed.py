from app import db
from models import Pet

db.drop_all()
db.create_all()

pet = Pet(name="waffle", species="dog", photo_url="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", age=2, notes="Smiley, small and golden brown.", available=True)

db.session.add(pet)
db.session.commit()

