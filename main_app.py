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
        if user['role'] == 'Community Health Worker':
            self.show_health_worker_dashboard(page, user)
        elif user['role'] == 'Veterinarian':
            self.show_veterinarian_dashboard(page, user)
        elif user['role'] == 'Resident':
            self.show_resident_dashboard(page, user)

    def show_health_worker_dashboard(self, page, user):
        # Health Worker Dashboard view
        page.views.clear()
        pet_list = self.get_pet_list()
        vaccination_records_list = self.get_vaccination_records_list()
        rabies_cases_list = self.get_rabies_cases_list()

        page.overlay.append(
            ft.AlertDialog(
                title=ft.Text("Welcome"),
                content=[
                    ft.Text(f"Welcome, {user['name']}!"),
                    ft.Text(f"Role: {user['role']}"),
                    # View Pets
                    ft.Text("View Pets"),
                    ft.ElevatedButton("View All Pets", on_click=lambda e: self.show_dialog(page, "All Pets", pet_list)),
                    ft.Divider(),
                    # View Vaccination Records
                    ft.Text("View Vaccination Records"),
                    ft.ElevatedButton("View All Vaccination Records", on_click=lambda e: self.show_dialog(page, "All Vaccination Records", vaccination_records_list)),
                    ft.Divider(),
                    # View Rabies Cases
                    ft.Text("View Rabies Cases"),
                    ft.ElevatedButton("View All Rabies Cases", on_click=lambda e: self.show_dialog(page, "All Rabies Cases", rabies_cases_list)),
                    ft.Divider(),
                    # Logout Button
                    ft.ElevatedButton("Logout", on_click=lambda e: self.show_login(page))
                ]
            )
        )

    def show_veterinarian_dashboard(self, page, user):
        # Veterinarian Dashboard view
        page.views.clear()
        pet_list = self.get_pet_list()
        vaccination_records_list = self.get_vaccination_records_list()

        page.overlay.append(
            ft.AlertDialog(
                title=ft.Text("Welcome"),
                content=[
                    ft.Text(f"Welcome, {user['name']}!"),
                    ft.Text(f"Role: {user['role']}"),
                    # View Pets
                    ft.Text("View Pets"),
                    ft.ElevatedButton("View All Pets", on_click=lambda e: self.show_dialog(page, "All Pets", pet_list)),
                    ft.Divider(),
                    # View Vaccination Records
                    ft.Text("View Vaccination Records"),
                    ft.ElevatedButton("View All Vaccination Records", on_click=lambda e: self.show_dialog(page, "All Vaccination Records", vaccination_records_list)),
                    ft.Divider(),
                    # Logout Button
                    ft.ElevatedButton("Logout", on_click=lambda e: self.show_login(page))
                ]
            )
        )

    def show_resident_dashboard(self, page, user):
        # Resident Dashboard view
        page.views.clear()
        page.overlay.append(
            ft.AlertDialog(
                title=ft.Text("Welcome"),
                content=[
                    ft.Text(f"Welcome, {user['name']}!"),
                    ft.Text(f"Role: {user['role']}"),
                    # Logout Button
                    ft.ElevatedButton("Logout", on_click=lambda e: self.show_login(page))
                ]
            )
        )

    def show_login(self, page):
        page.views.clear()
        page.overlay.append(
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

    def login(self, event, page):
        email = self.email_input.value
        password = self.password_input.value
        user = self.user_manager.authenticate_user(email, password)
        if user:
            page.overlay.append(
                ft.AlertDialog(title=ft.Text("Success"), content=[ft.Text("Login successful!")])
            )
            self.show_dashboard(page, user)
        else:
            page.overlay.append(
                ft.AlertDialog(title=ft.Text("Error"), content=[ft.Text("Invalid credentials!")])
            )

    def register(self, event, page):
        name = self.name_input.value
        email = self.email_reg_input.value
        password = self.password_reg_input.value
        role = self.role_dropdown.value
        self.user_manager.register_user(name, email, password, role)
        page.overlay.append(
            ft.AlertDialog(title=ft.Text("Success"), content=[ft.Text("Registration successful!")])
        )

    def get_pet_list(self):
        pets = self.db_manager.get_pets_collection().find({})
        pet_list = []
        for pet in pets:
            pet_list.append(f"Pet Name: {pet['pet_name']}, Species: {pet['species']}, Age: {pet['age']}")
        return pet_list

    def get_vaccination_records_list(self):
        vaccination_records = self.db_manager.get_vaccination_records_collection().find({})
        record_list = []
        for record in vaccination_records:
            record_list.append(f"Pet ID: {record['pet_id']}, Vaccine Name: {record['vaccine_name']}, Vaccination Date: {record['vaccination_date']}")
        return record_list

    def get_rabies_cases_list(self):
        rabies_cases = self.db_manager.get_rabies_cases_collection().find({})
        case_list = []
        for case in rabies_cases:
            case_list.append(f"Case Details: {case['case_details']}, Reported Date: {case['reported_date']}")
        return case_list

    def show_dialog(self, page, title, content_list):
        dialog_content = [ft.Text(item) for item in content_list]
        page.overlay.append(
            ft.AlertDialog(title=ft.Text(title), content=dialog_content)
        )

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
