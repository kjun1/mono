import random

from src.map import Map, Square, Event


# すごろくゲームのクラス
class Sugoroku:
    # すごろくの初期化
    def __init__(self, player_list, dice, map):
        # すごろくのプレイヤーリスト
        self.__player_list = player_list
        # すごろくのサイコロ
        self.__dice = dice
        # すごろくのマップ
        self.__map = map
    # すごろくのプレイヤーリストを設定する
    def set_player_list(self, player_list):
        self.__player_list = player_list
    # すごろくのプレイヤーリストを取得する
    def get_player_list(self):
        return self.__player_list
    # すごろくのサイコロを取得する
    def get_dice(self):
        return self.__dice
    # すごろくのマップを設定する
    def set_map(self, map):
        self.__map = map
    # すごろくのマップを取得する
    def get_map(self):
        return self.__map
    # すごろくのマップのマス目の数を取得する
    def get_map_size(self):
        return self.__map.get_map_size()
    
    # すごろくのメイン処理
    def main(self):
        # すごろくゲームの開始
        flg = True
        print("すごろくゲームを開始します")
        while flg:
            # プレイヤーのリストでループ
            for player in self.get_player_list():
                # サイコロを振る
                dice = self.get_dice()
                dice_eyes = dice.roll()
                # 駒を進める
                piece = player.get_piece()
                piece.set_position(piece.get_position() + dice_eyes)
                # マップのマス目の数以上になったら
                if piece.get_position() >= self.get_map_size():
                    # 駒の位置からマップのマス目の数を引く
                    piece.set_position(piece.get_position() - self.get_map_size())
                # マップのマス目のリストを取得する
                map = self.get_map()
                # マップのマス目のリストの駒の位置のマス目を取得する
                map_square = map[piece.get_position()]
                # マップのマス目のリストの駒の位置のマス目のイベントを実行する
                map_square.execute_event(player)
                # マップのマス目のリストの駒の位置のマス目のイベントの結果を取得する
                event_result = map_square.get_result()
                # マップのマス目のリストの駒の位置のマス目のイベントの結果がゴールの場合
                if event_result == "ゴール":
                    # すごろくゲームの終了
                    print("ゴール")
                    flg = False
                    break

# プレイヤーのクラス
class Player:
    # プレイヤーの初期化
    def __init__(self):
        # プレイヤーの名前
        self.__name = ""
        # プレイヤーのキャラクター
        self.__character = None
        # プレイヤーの駒
        self.__piece = Piece()
    # プレイヤーの名前を設定する
    def set_name(self, name):
        self.__name = name
    # プレイヤーの名前を取得する
    def get_name(self):
        return self.__name
    # プレイヤーのキャラクターを設定する
    def set_character(self, character):
        self.__character = character
    # プレイヤーのキャラクターを取得する
    def get_character(self):
        return self.__character
    # プレイヤーの駒を設定する
    def set_piece(self, piece):
        self.__piece = piece
    # プレイヤーの駒を取得する
    def get_piece(self):
        return self.__piece

# 駒のクラス
class Piece:
    # 駒の初期化
    def __init__(self):
        # 駒の位置
        self.__position = 0
    # 駒の位置を設定する
    def set_position(self, position):
        self.__position = position
    # 駒の位置を取得する
    def get_position(self):
        return self.__position

# キャラクターのクラス
class Character:
    # キャラクターの初期化
    def __init__(self):
        # キャラクターの名前
        self.__name = ""
    # キャラクターの名前を設定する
    def set_name(self, name):
        self.__name = name
    # キャラクターの名前を取得する
    def get_name(self):
        return self.__name

# さいころのクラス
class Dice:
    # さいころの初期化
    def __init__(self):
        # さいころの目の最大値
        self.__eyes = 6
    # さいころを振る
    def roll(self):
        return random.randint(1, self.__eyes)
    
# すごろくゲームのメインプログラム
if __name__ == "__main__":
    """
    すごろくゲームの初期化
    """
    # プレイヤーの初期化
    player_list = []
    # TODO: 仮置きでプレイヤーを3人作成
    for i in range(3):
        player = Player()
        player.set_name("プレイヤー" + str(i))
        # TODO: 仮置きで全部のプレイヤーが同じキャラクターを作成
        character = Character()
        character.set_name("キャラクター")
        player.set_character(character)
        player_list.append(player)

    # サイコロの初期化
    dice = Dice()

    # マップのマス目の初期化
    square_list = []
    # TODO: 仮置きでマス目を20個作成
    for i in range(20):
        square = Square()
        square.set_name("マス目" + str(i))
        square.set_number(i)
        # TODO: 仮置きでマス目のイベントを作成
        event = Event()
        event.set_effect("マス目" + str(i) + "のイベント")
        square.set_event(event)
        square_list.append(square)
    # TODO: 0番目のマス目の効果をゴールにする
    event.set_effect("ゴール")
    square_list[0].set_event(event)
    # マップの初期化
    map = Map(square_list)

    # すごろくの初期化
    sugoroku = Sugoroku(player_list, dice, map)
    # すごろくを実行する
    sugoroku.main()