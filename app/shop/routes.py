"""Public pages. Milestone 1 uses static sample data; Milestone 4 reads the DB."""
from flask import render_template
from . import bp

CATEGORIES = [
    ("Fruits", "🍎"), ("Vegetables", "🥦"), ("Dairy & Eggs", "🥛"),
    ("Bakery", "🍞"), ("Grains & Staples", "🌾"), ("Snacks", "🥜"),
    ("Beverages", "🧃"), ("Household", "🧼"),
]
SAMPLE_PRODUCTS = [
    {"id": 1, "name": "Fresh Bananas", "price": "55.00", "unit": "dozen", "stock": 40},
    {"id": 2, "name": "Tomatoes", "price": "32.00", "unit": "kg", "stock": 60},
    {"id": 3, "name": "Full Cream Milk", "price": "34.00", "unit": "500 ml", "stock": 3},
    {"id": 4, "name": "Brown Bread", "price": "45.00", "unit": "packet", "stock": 25},
    {"id": 5, "name": "Basmati Rice", "price": "145.00", "unit": "kg", "stock": 0},
    {"id": 6, "name": "Farm Eggs", "price": "78.00", "unit": "dozen", "stock": 30},
]


@bp.route("/")
def home():
    return render_template("home.html", categories=CATEGORIES, products=SAMPLE_PRODUCTS)


@bp.route("/shop")
def shop():
    return render_template("shop.html", categories=CATEGORIES, products=SAMPLE_PRODUCTS)


@bp.route("/about")
def about():
    return render_template("about.html")
