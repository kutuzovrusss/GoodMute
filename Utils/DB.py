import sqlite3


class Get:
    def __init__(self):
        pass

    def mute(self, member):
        conn = sqlite3.connect("./Data/DataBase/members_mutes.db")
        cursor = conn.cursor()

        if member:
            cursor.execute(f"SELECT * FROM mutes WHERE member={member.id}")
            result = cursor.fetchone()
        else:
            cursor.execute(f"SELECT * FROM mutes")
            result = cursor.fetchall()

        return result


class Set:
    def __init__(self):
        pass

    def mute(self, member, time):
        conn = sqlite3.connect("./Data/DataBase/members_mutes.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM mutes")
        if not cursor.fetchone():
            cursor.execute(f"INSERT INTO mutes VALUES ({member.id}, 0)")
        else:
            cursor.execute(f"UPDATE mutes SET time = {time} WHERE member='{member.id}'")

        conn.commit()
        conn.close()
