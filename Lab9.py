import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = datetime.now()

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M')}"

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Книга Заметок")

        self.notes = []

        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(pady=20)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Добавить", command=self.add_note)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Редактировать", command=self.edit_note)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Удалить", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.sort_button = tk.Button(self.button_frame, text="Сортировать", command=self.sort_notes)
        self.sort_button.pack(side=tk.LEFT, padx=5)

    def add_note(self):
        title = simpledialog.askstring("Заголовок", "Введите заголовок заметки:")
        if title:
            content = simpledialog.askstring("Содержание", "Введите содержание заметки:")
            if content:
                note = Note(title, content)
                self.notes.append(note)
                self.update_listbox()

    def edit_note(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            note = self.notes[index]
            new_title = simpledialog.askstring("Изменить заголовок", "Введите новый заголовок:", initialvalue=note.title)
            if new_title:
                new_content = simpledialog.askstring("Изменить содержание", "Введите новое содержание:", initialvalue=note.content)
                if new_content:
                    note.title = new_title
                    note.content = new_content
                    self.update_listbox()

    def delete_note(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.notes[index]
            self.update_listbox()

    def sort_notes(self):
        self.notes.sort(key=lambda note: note.date)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for note in self.notes:
            self.listbox.insert(tk.END, str(note))

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()

