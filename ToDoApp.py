import unittest

# Model for a simple TODO list application
class TodoListModel:
    def __init__(self):
        self.items = []
        self.add_button_enabled = False

    def enter_text(self, text):
        if text:
            self.add_button_enabled = True
        else:
            self.add_button_enabled = False

    def add_item(self, item_name):
        if self.add_button_enabled:
            self.items.append(item_name)
            self.add_button_enabled = False  # Reset the button state


# Story: TODOリストにタスクを追加する

class Rule_追加ボタンはテキストフィールドにテキストが入力されている場合に活性化する(unittest.TestCase):
    def test_テキストフィールドに1文字入力された場合_追加ボタンが活性化する(self):
        model = TodoListModel()
        model.enter_text('A')
        self.assertTrue(model.add_button_enabled)

    def test_テキストフィールドが空の場合_追加ボタンが非活性になる(self):
        model = TodoListModel()
        model.enter_text('')
        self.assertFalse(model.add_button_enabled)


class Rule_追加ボタンを押下すると項目が追加される(unittest.TestCase):
    def test_追加ボタンを押下するとTODOリストにタスクが追加される(self):
        model = TodoListModel()
        model.enter_text('New Task')
        model.add_item('New Task')
        self.assertIn('New Task', model.items)


class Rule_テキストフィールドに入力されたテキストがタスク名となる(unittest.TestCase):
    def test_テキストフィールドにAAAを入力し追加ボタンを押下すると追加されたタスク名はAAAとなる(self):
        model = TodoListModel()
        model.enter_text('AAA')
        model.add_item('AAA')
        self.assertIn('AAA', model.items)


# Running the tests
unittest.main(argv=[''], exit=False)
