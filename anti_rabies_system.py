import bcrypt
import flet as ft
from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["anti_rabies_db"]

# Collections
users_collection = db["users"]
pets_collection = db["pets"]
vaccination_records_collection = db["vaccination_records"]
rabies_cases_collection = db["rabies_cases"]

# Utility functions
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# User Registration
def register_user(name, email, password, role):
    hashed_password = hash_password(password)
    user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role
    }
    users_collection.insert_one(user)

# User Authentication
def authenticate_user(email, password):
    user = users_collection.find_one({"email": email})
    if user and check_password(password, user["password"]):
        return user
    return None

# Main UI
def main(page):
    def login(event):
        email = email_input.value
        password = password_input.value
        user = authenticate_user(email, password)
        if user:
            page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Login successful!"))
            page.dialog.open = True
            show_dashboard(user)
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Error"), content=ft.Text("Invalid credentials!"))
            page.dialog.open = True
        page.update()

    def register(event):
        name = name_input.value
        email = email_reg_input.value
        password = password_reg_input.value
        role = role_dropdown.value
        register_user(name, email, password, role)
        page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Registration successful!"))
        page.dialog.open = True
        page.update()

    def show_dashboard(user):
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Text(f"Welcome, {user['name']}!"),
                    ft.Text(f"Role: {user['role']}"),
                    # Add more dashboard controls based on user role
                    ft.ElevatedButton("Logout", on_click=lambda e: show_login())
                ]
            )
        )
        page.update()

    def show_login():
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Text("Anti-Rabies Database System", style="headline1"),
                    ft.Text("Login"),
                    email_input,
                    password_input,
                    ft.ElevatedButton("Login", on_click=login),
                    ft.Divider(),
                    ft.Text("Register"),
                    name_input,
                    email_reg_input,
                    password_reg_input,
                    role_dropdown,
                    ft.ElevatedButton("Register", on_click=register),
                ]
            )
        )
        page.update()

    # Define inputs
    email_input = ft.TextField(label="Email")
    password_input = ft.TextField(label="Password", password=True)
    name_input = ft.TextField(label="Name")
    email_reg_input = ft.TextField(label="Email")
    password_reg_input = ft.TextField(label="Password", password=True)
    role_dropdown = ft.Dropdown(
        label="Role",
        options=[
            ft.dropdown.Option("Community Health Worker"),
            ft.dropdown.Option("Veterinarian"),
            ft.dropdown.Option("Resident")
        ]
    )

    # Show login view
    show_login()

ft.app(target=main)
