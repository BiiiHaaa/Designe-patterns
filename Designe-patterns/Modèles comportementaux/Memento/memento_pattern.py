# Memento (Stores State)
class Memento:
    def __init__(self, state):
        self.state = state

# Originator (Creates and Restores Mementos)
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content = text

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.state

    def get_content(self):
        return self._content

# Caretaker (Manages Mementos)
class History:
    def __init__(self):
        self._mementos = []

    def save(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None

# Client Code
editor = TextEditor()
history = History()

# Writing and Saving States
editor.write("Hello, World!")
history.save(editor.save())

editor.write("Hello, Python!")
history.save(editor.save())

editor.write("Hello, Design Patterns!")

print("Current Content:", editor.get_content())  # Hello, Design Patterns!

# Undo Changes
editor.restore(history.undo())
print("After Undo:", editor.get_content())  # Hello, Python!

editor.restore(history.undo())
print("After Second Undo:", editor.get_content())  # Hello, World!
