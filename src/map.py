# マップのクラス
class Map:
    # マップの初期化
    def __init__(self, square_list):
        # マップのマス目のリスト
        self.__map = square_list
        # マップのマス目の数
        self.__map_size = len(square_list)
    # マップのマス目を設定する
    def set_map(self, square_list):
        self.__map = square_list
        self.__map_size = len(square_list)
    # マップのマス目のリストを取得する
    def get_map(self):
        return self.__map
    # マップのマス目の数を取得する
    def get_map_size(self):
        return self.__map_size
    # インデックス指定されたマス目を返す
    def __getitem__(self, index):
        return self.__map[index]
    
    
# マス目のクラス
class Square:
    # マス目の初期化
    def __init__(self):
        # マス目の名前
        self.__name = ""
        # マス目の番号
        self.__number = -1
        # マス目のイベント
        self.__event = None
    # マス目の名前を設定する
    def set_name(self, name):
        self.__name = name
    # マス目の名前を取得する
    def get_name(self):
        return self.__name
    # マス目の番号を設定する
    def set_number(self, number):
        self.__number = number
    # マス目の番号を取得する
    def get_number(self):
        return self.__number
    # マス目のイベントを設定する
    def set_event(self, event):
        self.__event = event
    # マス目のイベントを取得する
    def get_event(self):
        return self.__event
    # マス目のイベントを実行する
    def execute_event(self, player):
        self.__event.execute(player)
    # マス目のイベントの結果を取得する
    def get_result(self):
        return self.__event.get_result()
    
# マス目のイベントのクラス
class Event:
    # マス目のイベントの初期化
    def __init__(self):
        # マス目のイベントの結果
        self.__effect = ""
    # マス目のイベントを実行する
    def execute(self, player):
        pass
    # マス目のイベントの結果を取得する
    def get_result(self):
        # TODO: 仮置きで効果を直接返す
        return self.get_effect()
    # マス目のイベントの効果を取得する
    def get_effect(self):
        return self.__effect
    # マス目のイベントの効果を設定する
    def set_effect(self, effect):
        self.__effect = effect
