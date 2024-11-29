# Memento Class
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


# Originator Class
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text: str):
        self._content += text

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento):
        self._content = memento.get_state()

    def get_content(self) -> str:
        return self._content


# Caretaker Class
class History:
    def __init__(self):
        self._history = []

    def push(self, memento: Memento):
        self._history.append(memento)

    def pop(self) -> Memento:
        if not self._history:
            return None
        return self._history.pop()


# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    # Write and save content
    editor.write("Hello, ")
    history.push(editor.save())  # Save state

    editor.write("World!")
    history.push(editor.save())  # Save state

    editor.write(" This is Python.")
    print("Current Content:", editor.get_content())

    # Undo operation
    editor.restore(history.pop())
    print("After Undo:", editor.get_content())

    editor.restore(history.pop())
    print("After Another Undo:", editor.get_content())
