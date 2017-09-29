import pickle

class Database:

    tmp_db = []

    def __init__(self, db_filename):
        self.db_name = db_filename
        try:
            f = open(self.db_name, "rb")
        except FileNotFoundError:
            print("New db: {}".format(self.db_name))
        else:
            print("Open db: {}".format(self.db_name))
            try:
                self.tmp_db = pickle.load(f)
            except EOFError:
                print("Empty db: {}".format(self.db_name))
            finally:
                f.close()

    def show(self, *args):
        for row in sorted(self.tmp_db, key=lambda row: row['Name']):
            for info in sorted(row):
                print(info + "=" + row[info], end=' ')
            print()

    def add(self, user_input):
        try:
            command, age, name, score = user_input.split()
        except ValueError:
            print("Please input correctly.")
        else:
            self.tmp_db += [{"Age": age, "Name": name, "Score": score}]

    def delete(self, user_input):
        name = user_input.split()[1]

        for row in self.tmp_db:
            if row.get("Name") == name:
                self.tmp_db.remove(self.tmp_db[self.tmp_db.index(row)])

    def quit_db(self, *args):
        from sys import exit
        exit()

    def inc(self, user_input):
        name, amount = user_input.split()[1], user_input.split()[2]

        for row in self.tmp_db:
            if row.get("Name") == name:
                self.tmp_db[self.tmp_db.index(row)]["Score"] = str(int(row["Score"]) + int(amount))
                break

    def find(self, user_input):
        name = user_input.split()[1]

        for row in self.tmp_db:
            if row.get("Name") == name:
                print(row)
                return None

        print("There's no {}".format(name))

    def save(self, *args):
        f = open(self.db_name, "wb")
        pickle.dump(self.tmp_db, f)
        f.close()

    def run(self):
        while True:
            user_input = input()
            command = {
                "add": self.add,
                "show": self.show,
                "del": self.delete,
                "quit": self.quit_db,
                "inc": self.inc,
                "find": self.find,
                "save": self.save
            }

            try:
                command[user_input.split()[0]](user_input)
            except KeyError:
                print("Please input correctly.")

if __name__ == "__main__":
    db = Database("aa.txt")
    db.run()
