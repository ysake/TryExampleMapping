import unittest



# Model for a simple TODO list application

class TodoListModel:
    def __init__(self):
        self.items = []
        self.selectedItemIndices = []  # 複数選択用のリスト
        self.add_button_enabled = False
        self.trush_button_enabled = False

    def enter_text(self, text):
        self.add_button_enabled = bool(text)

    def add_item(self, item_name):
        if self.add_button_enabled:
            self.items.append(item_name)
            self.add_button_enabled = False

    def toggle_selection(self, item_name):
        try:
            index = self.items.index(item_name)
            if index in self.selectedItemIndices:
                self.selectedItemIndices.remove(index)
            else:
                self.selectedItemIndices.append(index)
            self.update_trush_button_state()
        except ValueError:
            pass

    def update_trush_button_state(self):
        self.trush_button_enabled = len(self.selectedItemIndices) > 0

    def push_trash_button(self):
        for index in sorted(self.selectedItemIndices, reverse=True):
            if index < len(self.items):
                self.items.pop(index)
        self.selectedItemIndices = []


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
    def test_タスク2を選択しゴミ箱ボタンを押下_タスク2が削除される_タスク1と3は残る(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        model.toggle_selection('Task2')
        model.push_trash_button()
        self.assertNotIn('Task2', model.items)
        self.assertIn('Task1', model.items)
        self.assertIn('Task3', model.items)

# - タスクが3つ存在する場合タスクを3つ選んでゴミ箱ボタンを押下するとタスクが全て消える
class Rule_複数のタスクを選択しゴミ箱を押下すると複数のタスクが削除される(unittest.TestCase):
    def test_タスク1から3を選択しゴミ箱ボタンを押下_タスク1から3が削除される(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        model.toggle_selection('Task1')
        model.toggle_selection('Task2')        
        model.toggle_selection('Task3')
        model.push_trash_button()
        self.assertEqual(len(model.items), 0)

# - タスクが選択されていない時はゴミ箱ボタンは非活性になる
class Rule_タスクが選択されていない時はゴミ箱ボタンは非活性になる(unittest.TestCase):
    def test_タスク1から3の何も選択されていない_ゴミ箱ボタンが非活性である(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        self.assertFalse(model.trush_button_enabled)

    def test_タスク1が選択されている_ゴミ箱ボタンが活性である(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        model.toggle_selection('Task1')
        self.assertTrue(model.trush_button_enabled)

# - 全てのチェックボックスが未選択の場合はゴミ箱ボタンが非活性になる
class Rule_全てのチェックボックスが未選択の場合はゴミ箱ボタンが非活性になる(unittest.TestCase):
    def test_タスク1を選択後_選択を外した時_ゴミ箱ボタンは非活性である(self):
        model = TodoListModel()
        model.items = ['Task1', 'Task2', 'Task3']
        model.toggle_selection('Task1')
        model.toggle_selection('Task1')
        self.assertFalse(model.trush_button_enabled)

# - 連打しても変な挙動にならない
# 　- タスク削除後にゴミ箱ボタンが非活性化すること
#   - タスク削除後にいずれのラジオボタンも選択されていないこと
# - タスクは何個まで？

# Story: 削除したタスクを復元できる

# Running the tests
unittest.main(argv=[''], exit=False)
