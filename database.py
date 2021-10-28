import sqlite3

class DataBase:

    def __init__(self):
        self.con = sqlite3.connect(r'database/vfat_1.db')
        self.cur = self.con.cursor()


    def creat_tables(self):

    	self.cur.execute("""CREATE TABLE IF NOT EXISTS user_key (tele_token TEXT, user_key TEXT)""")
		self.cur.execute("""CREATE TABLE IF NOT EXISTS user_boards (user_key TEXT, board_id TEXT)""")
		self.cur.execute("""CREATE TABLE IF NOT EXISTS board_info (board_id TEXT, message_type INTEGER)""")


	def set_user_key_data(self, data):

		self.cur.execute("""INSERT INTO user_key VALUES (?, ?)""", data)
		self.con.commit()

	def set_user_board_data(self, data):

		self.cur.execute("""INSERT INTO user_boards VALUES (?, ?)""", data)
		self.con.commit()

	def set_board_info_data(self, data):

		self.cur.execute("""INSERT INTO board_info VALUES (?, ?)""", data)
		self.con.commit()