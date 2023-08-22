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
        # マス目通過時イベント
        self.__event_pass = None
        # マス目到達時イベント
        self.__event_arrive = None
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
    # マス目通過時イベントを設定する
    def set_event_pass(self, event_pass):
        self.__event_pass = event_pass
    # マス目通過時イベントを取得する
    def get_event_pass(self):
        return self.__event_pass
    # マス目到達時イベントを設定する
    def set_event_arrive(self, event_arrive):
        self.__event_arrive = event_arrive
    # マス目到達時イベントを取得する
    def get_event_arrive(self):
        return self.__event_arrive
    # マス目通過時イベントを実行する
    def execute_event_pass(self, player):
        if self.__event_pass != None:
            self.__event_pass.execute(player)
    # マス目到達時イベントを実行する
    def execute_event_arrive(self, player):
        if self.__event_arrive != None:
            self.__event_arrive.execute(player)

    
# マス目のイベントのクラス
class Event:
    # マス目のイベントの初期化
    def __init__(self):
        # マス目のイベントの種類
        self.__type = ""
        # マス目のイベントの効果
        self.__effect = None
    # マス目のイベントを実行する
    def execute(self, player):
        # プレイヤーに効果を実行する
        text = self.__effect(player)
        # テキストを返す
        return text
    # マス目のイベントの種類を設定する
    def set_type(self, type):
        self.__type = type
    # マス目のイベントの種類を取得する
    def get_type(self):
        return self.__type
    # マス目のイベントの効果を設定する
    def set_effect(self, effect):
        self.__effect = effect
    # マス目のイベントの効果を取得する
    def get_effect(self):
        return self.__effect
    
    
