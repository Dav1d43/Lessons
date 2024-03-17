import sys
import json
from diarybook import Diarybook, Diary

class Menu:
    def __init__(self):
        self.diarybook = Diarybook()
        self.choices = {
            "1": self.show_all_diaries,
            "2": self.add_diaries,
            "3": self.search_diaries,
            "4": self.sort_diaries,
            "5": self.populate_database,
            "6": self.account_management,
            "7": self.save_diaries_to_json,
            "8": self.quit
        }
        self.users = self.load_users()

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries in the database")
        for diary in self.diarybook.diaries:
            print(f"{diary.id} - {diary.memo}")

    def add_diaries(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.diarybook.new_diary(memo, tags)
        print("Your note has been added successfully")
        self.save_diaries_to_json()

    def search_diaries(self):
        keyword = input("Enter a keyword: ")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("No matching diaries found.")
        for diary in filtered_diaries:
            print(f"{diary.id} - {diary.memo}")

    def sort_diaries(self):
        sort_option = input("Sort by (id/memo): ").lower()
        if sort_option == "id":
            self.diarybook.diaries.sort(key=lambda x: x.id)
        elif sort_option == "memo":
            self.diarybook.diaries.sort(key=lambda x: x.memo)
        else:
            print("Invalid sort option")

    def populate_database(self):
        diaries = self.read_from_json_into_app("data.json")
        self.diarybook.diaries.extend(diaries)

    def account_management(self):
        print("1. Register\n2. Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.register_user()
        elif choice == "2":
            self.login_user()
        else:
            print("Invalid choice")

    def register_user(self):
        username = input("Enter username: ")
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return
        password = input("Enter password: ")
        self.users[username] = password
        self.save_users()
        print("Registration successful.")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password.")


    def load_users(self):
        try:
            with open("users.json") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def read_from_json_into_app(path):
        with open(path) as file:
            data = json.load(file)
            diaries = [Diary(entry["memo"], entry["tags"]) for entry in data]
            return diaries

    def save_diaries_to_json(self):
        diaries_data = [{"memo": diary.memo, "tags": diary.tags} for diary in self.diarybook.diaries]
        with open("data.json", "w") as file:
            json.dump(diaries_data, file)

    def quit(self):
        print("Thank you")
        sys.exit()

    def display_menu(self):
        print("""
        Diarybook Menu:

        1. Show diaries
        2. Add diaries
        3. Filter using keyword
        4. Sort diaries
        5. Populate database
        6. Account Management
        7. Save diaries to JSON
        8. Quit program
        """)

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = input("Enter a choice: ")
                action = self.choices.get(choice)
                if action:
                    action()
                else:
                    print(f"{choice} isn't a valid choice")
        except Exception as e:
            print("Error:", e)
            self.quit()

if __name__ == "__main__":
    Menu().run()
