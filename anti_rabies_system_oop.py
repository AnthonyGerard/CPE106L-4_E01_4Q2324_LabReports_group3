import flet as ft

class MainApp:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.user_manager = User(self.db_manager)
        self.pet_manager = Pet(self.db_manager)
        self.vaccination_record_manager = VaccinationRecord(self.db_manager)

    def main(self, page):
        def login(event):
            email = email_input.value
            password = password_input.value
            user = self.user_manager.authenticate_user(email, password)
            if user:
                page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Login successful!"))
                page.dialog.open = True
                self.show_dashboard(page, user)
            else:
                page.dialog = ft.AlertDialog(title=ft.Text("Error"), content=ft.Text("Invalid credentials!"))
                page.dialog.open = True
            page.update()

        def register(event):
            name = name_input.value
            email = email_reg_input.value
            password = password_reg_input.value
            role = role_dropdown.value
            self.user_manager.register_user(name, email, password, role)
            page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Registration successful!"))
            page.dialog.open = True
            page.update()

        def save_pet(event):
            pet_name = pet_name_input.value
            species = species_input.value
            age = age_input.value
            vaccination_status = vaccination_status_input.value
            self.pet_manager.add_pet(user['_id'], pet_name, species, age, vaccination_status)
            page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Pet added successfully!"))
            page.dialog.open = True
            page.update()

        def save_vaccination_record(event):
            pet_id = pet_id_input.value
            vaccine_name = vaccine_name_input.value
            vaccination_date = vaccination_date_input.value
            veterinarian_id = user['_id']
            self.vaccination_record_manager.add_vaccination_record(pet_id, vaccine_name, vaccination_date, veterinarian_id)
            page.dialog = ft.AlertDialog(title=ft.Text("Success"), content=ft.Text("Vaccination record added successfully!"))
            page.dialog.open = True
            page.update()

        def show_dashboard(page, user):
            pet_name_input = ft.TextField(label="Pet Name")
            species_input = ft.TextField(label="Species")
            age_input = ft.TextField(label="Age")
            vaccination_status_input = ft.TextField(label="Vaccination Status")

            pet_id_input = ft.TextField(label="Pet ID")
            vaccine_name_input = ft.TextField(label="Vaccine Name")
            vaccination_date_input = ft.TextField(label="Vaccination Date")

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
                        ft.ElevatedButton("Save Pet", on_click=save_pet),
                        ft.Divider(),
                        # Add Vaccination Record Form
                        ft.Text("Add Vaccination Record"),
                        pet_id_input,
                        vaccine_name_input,
                        vaccination_date_input,
                        ft.ElevatedButton("Save Vaccination Record", on_click=save_vaccination_record),
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

if __name__ == "__main__":
    app = MainApp()
    ft.app(target=app.main)
