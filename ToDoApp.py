import unittest



# Model for a simple TODO list application

class TodoListModel:
    def __init__(self):
        self.items = []
        self.selectedItemIndex = None
        self.add_button_enabled = False

    def enter_text(self, text):
        self.add_button_enabled = bool(text)

    def add_item(self, item_name):
        if self.add_button_enabled:
            self.items.append(item_name)
            self.add_button_enabled = False  # Reset the button state

    def select(self, selected_item_name):
        try:
            self.selectedItemIndex = self.items.index(selected_item_name)
        except ValueError:
            self.selectedItemIndex = None
    
    def push_trash_button(self):
        if self.selectedItemIndex is not None and self.selectedItemIndex < len(self.items):
            self.items.pop(self.selectedItemIndex)
            self.selectedItemIndex = None



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

class Rule_追加ボタンを押下するとタスクが追加される(unittest.TestCase):
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

# Story: TODOリストのタスクを削除できる

# - ゴミ箱ボタンを押下すると選択されたタスクが削除される
class Rule_ゴミ箱ボタンを押下すると選択されたタスクが削除される(unittest.TestCase):
    def test_タスク2を選択しゴミ箱ボタンを押下_タスク2が削除される(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        model.select('Task2')
        model.push_trash_button()
        self.assertNotIn('Task2', model.items)

# - タスクが3つ存在する場合タスクを3つ選んでゴミ箱ボタンを押下するとタスクが全て消える
# - タスクが選択されていない時はゴミ箱ボタンは非活性になる
# - 連打しても変な挙動にならない
# 　- タスク削除後にゴミ箱ボタンが非活性化すること
#   - タスク削除後にいずれのラジオボタンも選択されていないこと
# - タスク2を選択しゴミ箱を押す
#   - タスク2が削除される
#   - タスク1とタスク3は残る

# - タスクは何個まで？

# Story: 削除したタスクを復元できる

# Running the tests
unittest.main(argv=[''], exit=False)
