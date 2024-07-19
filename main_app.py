import flet as ft
from database_manager import DatabaseManager
from user import User
from pet import Pet
from vaccination_record import VaccinationRecord
from rabies_case import RabiesCase

class MainApp:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.user_manager = User(self.db_manager)
        self.pet_manager = Pet(self.db_manager)
        self.vaccination_record_manager = VaccinationRecord(self.db_manager)
        self.rabies_case_manager = RabiesCase(self.db_manager)

    def show_dashboard(self, page, user):
        pet_name_input = ft.TextField(label="Pet Name")
        species_input = ft.TextField(label="Species")
        age_input = ft.TextField(label="Age")
        vaccination_status_input = ft.TextField(label="Vaccination Status")

        pet_id_input = ft.TextField(label="Pet ID")
        vaccine_name_input = ft.TextField(label="Vaccine Name")
        vaccination_date_input = ft.TextField(label="Vaccination Date")

        case_details_input = ft.TextField(label="Case Details")
        reported_date_input = ft.TextField(label="Reported Date")

        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Text(f"Welcome, {user['name']}!"),
                    ft.Text(f"Role: {user['role']}"),
                    # Add Pet Form
                    ft.Text("Add Pet"),
                    pet_name_input,
                    species_input,
                    age_input,
                    vaccination_status_input,
                    ft.ElevatedButton("Save Pet", on_click=lambda e: self.save_pet(e, pet_name_input, species_input, age_input, vaccination_status_input, user, page)),
                    ft.Divider(),
                    # Add Vaccination Record Form
                    ft.Text("Add Vaccination Record"),
                    pet_id_input,
                    vaccine_name_input,
                    vaccination_date_input,
                    ft.ElevatedButton("Save Vaccination Record", on_click=lambda e: self.save_vaccination_record(e, pet_id_input, vaccine_name_input, vaccination_date_input, user, page)),
                    ft.Divider(),
                    # Add Rabies Case Form
                    ft.Text("Add Rabies Case"),
                    case_details_input,
                    reported_date_input,
                    ft.ElevatedButton("Save Rabies Case", on_click=lambda e: self.save_rabies_case(e, case_details_input, reported_date_input, user, page)),
                    # Add more dashboard controls based on user role
                    ft.ElevatedButton("Logout", on_click=lambda e: self.show_login(page))
                ]
            )
        )
        page.update()

    def show_login(self, page):
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Text("Anti-Rabies Database System", style="headline1"),
                    ft.Text("Login"),
                    self.email_input,
                    self.password_input,
                    ft.ElevatedButton("Login", on_click=lambda e: self.login(e, page)),
                    ft.Divider(),
                    ft.Text("Register"),
                    self.name_input,
                    self.email_reg_input,
                    self.password_reg_input,
                    self.role_dropdown,
                    ft.ElevatedButton("Register", on_click=lambda e: self.register(e, page)),
                ]
            )
        )
        page.update()

    def login(self, event, page):
        email = self.email_input.value
        password = self.password_input.value
        user = self.user_manager.authenticate_user(email, password)
        if user:
            page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Login successful!"))
            page.dialog.open = True
            self.show_dashboard(page, user)
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Error"), content=ft.Text("Invalid credentials!"))
            page.dialog.open = True
        page.update()

    def register(self, event, page):
        name = self.name_input.value
        email = self.email_reg_input.value
        password = self.password_reg_input.value
        role = self.role_dropdown.value
        self.user_manager.register_user(name, email, password, role)
        page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Registration successful!"))
        page.dialog.open = True
        page.update()

    def save_pet(self, event, pet_name_input, species_input, age_input, vaccination_status_input, user, page):
        pet_name = pet_name_input.value
        species = species_input.value
        age = age_input.value
        vaccination_status = vaccination_status_input.value
        self.pet_manager.add_pet(user['_id'], pet_name, species, age, vaccination_status)
        page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Pet added successfully!"))
        page.dialog.open = True
        page.update()

    def save_vaccination_record(self, event, pet_id_input, vaccine_name_input, vaccination_date_input, user, page):
        pet_id = pet_id_input.value
        vaccine_name = vaccine_name_input.value
        vaccination_date = vaccination_date_input.value
        veterinarian_id = user['_id']
        self.vaccination_record_manager.add_vaccination_record(pet_id, vaccine_name, vaccination_date, veterinarian_id)
        page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Vaccination record added successfully!"))
        page.dialog.open = True
        page.update()

    def save_rabies_case(self, event, case_details_input, reported_date_input, user, page):
        case_details = case_details_input.value
        reported_date = reported_date_input.value
        reporter_id = user['_id']
        self.rabies_case_manager.add_rabies_case(reporter_id, case_details, reported_date)
        page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Rabies case added successfully!"))
        page.dialog.open = True
        page.update()

    def main(self, page):
        self.email_input = ft.TextField(label="Email")
        self.password_input = ft.TextField(label="Password", password=True)
        self.name_input = ft.TextField(label="Name")
        self.email_reg_input = ft.TextField(label="Email")
        self.password_reg_input = ft.TextField(label="Password", password=True)
        self.role_dropdown = ft.Dropdown(
            label="Role",
            options=[
                ft.dropdown.Option("Community Health Worker"),
                ft.dropdown.Option("Veterinarian"),
                ft.dropdown.Option("Resident")
            ]
        )
        self.show_login(page)

if __name__ == "__main__":
    app = MainApp()
    ft.app(target=app.main)
