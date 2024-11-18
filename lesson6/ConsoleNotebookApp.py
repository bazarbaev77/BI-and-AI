import csv
import datetime

class Note:
    def __init__(self, note_id, content, created):
        self.id = note_id
        self.content = content
        self.created = created

    def preview(self, length=30):
        return self.content[:length] + "..." if len(self.content) > length else self.content

class NoteManager:
    def __init__(self, filename="notes.csv"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        notes = []
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                for row in csv.reader(file):
                    if len(row) >= 3:  
                        notes.append(Note(int(row[0]), row[1], row[2]))
        except FileNotFoundError:
            print(f"{self.filename} not found, starting with an empty list of notes.")
        except ValueError as e:
            print(f"Error processing file contents: {e}")
        return notes

    def save_notes(self):
        with open(self.filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows([[note.id, note.content, note.created] for note in self.notes])

    def add_note(self, content):
        note_id = self.notes[-1].id + 1 if self.notes else 1
        created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(Note(note_id, content, created))
        self.save_notes()

    def update_note_content(self, note_id, new_content):
        note = self.get_note_by_id(note_id)
        if note:
            note.content = new_content
            self.save_notes()
            return True
        return False

    def delete_note_by_id(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

class NoteApp:
    def __init__(self):
        self.manager = NoteManager()

    def display_menu(self):
        print("\n1: Show All Notes\n2: View Note Details\n3: Create Note")
        print("4: Update Note\n5: Delete Note\n6: Quit")

    def handle_choice(self, choice):
        actions = {
            "1": self.show_all_notes,
            "2": self.view_note_details,
            "3": self.create_note,
            "4": self.update_note,
            "5": self.delete_note,
            "6": self.quit_app
        }
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")

    def show_all_notes(self):
        print("\nAll Notes:")
        for note in self.manager.notes:
            print(f"{note.id}. {note.preview()}")
        self.return_to_menu()

    def view_note_details(self):
        note_id = input("Enter note ID: ")
        note = self.manager.get_note_by_id(int(note_id))
        if note:
            print(f"\nNote {note.id}: {note.content}\nCreated: {note.created}\n")
        else:
            print("Note not found.")
        self.return_to_menu()

    def create_note(self):
        content = input("Enter note content: ")
        self.manager.add_note(content)
        print("Note added.")
        self.return_to_menu()

    def update_note(self):
        note_id = input("Enter note ID to update: ")
        new_content = input("Enter new content: ")
        if self.manager.update_note_content(int(note_id), new_content):
            print("Note updated.")
        else:
            print("Note not found.")
        self.return_to_menu()

    def delete_note(self):
        note_id = input("Enter note ID to delete: ")
        self.manager.delete_note_by_id(int(note_id))
        print("Note deleted.")
        self.return_to_menu()

    def return_to_menu(self):
        input("Press Enter to return to the menu...")

    def quit_app(self):
        print("Goodbye!")
        exit()

    def run(self):
        while True:
            self.display_menu()
            self.handle_choice(input("Choose an option: "))

if __name__ == "__main__":
    NoteApp().run()
