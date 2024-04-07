from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "dfdvknerot34iuh4t39hi"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
connect_db(app)
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """Homepage - Displays all pets in our pets_db database.Specifically, their photo, name and availibility."""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """GET and POST routes to render and post a form for adding a new pet."""

    form = PetForm()

    if form.validate_on_submit():

        # collect information from the PetForm
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data in ['True']

        # commit pet to the database
        new_pet  = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        # flash a success message for creating a pet
        flash(f"Successfully added {name} :)")
        
        return redirect("/")

    else:

        # if the form was not validated / properly filled out, rerender the form.
        return render_template("pet_form.html", form=form)

@app.route("/<int:id>", methods=["GET", "POST"])
def display_edit_pet(id):
    """GET and POST routes to render a pet and post an edited form submission."""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm()

    if form.validate_on_submit():

        # collect deited information from the EditPetForm
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data in ['True']

        db.session.commit()

        # flash a success message for editing a pet
        flash(f"Successfully edited {form.name.data} :)")
        
        return redirect("/")

    else:

        # pre fill out the form with the pet's information to make editing easier
        form.name.default = pet.name if pet else ''
        form.species.default = pet.species if pet else ''
        form.photo_url.default = pet.photo_url if pet else ''
        form.age.default = pet.age if pet else ''
        form.notes.default = pet.notes if pet else ''
        form.available.default = pet.available if pet else ''
        form.process()
        
        # if the form was not validated / properly filled out, rerender the form.
        return render_template("display_edit_form.html", form=form, pet=pet)