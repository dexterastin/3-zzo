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

    def show(self, user_input):
        key = user_input.split().pop()
        print(key)
        for row in sorted(self.tmp_db, key=lambda row: row[key[0].upper() + key[1:].lower()]):
            for info in sorted(row):
                print(info + "=" + row[info], end=' ')
            print()

        return self.tmp_db

    def add(self, user_input):
        try:
            command, age, name, score, key = user_input.split()
        except ValueError:
            return "Please input correctly."
        else:
            self.tmp_db += [{"Age": age, "Name": name, "Score": score}]
            return self.show(user_input)

    def delete(self, user_input):
        name = user_input.split()[1]

        for row in self.tmp_db:
            if row.get("Name") == name:
                self.tmp_db.remove(self.tmp_db[self.tmp_db.index(row)])

        return self.show(user_input)

    def quit_db(self, *args):
        from sys import exit
        exit()

    def inc(self, user_input):
        name, amount = user_input.split()[1], user_input.split()[2]

        for row in self.tmp_db:
            if row.get("Name") == name:
                self.tmp_db[self.tmp_db.index(row)]["Score"] = str(int(row["Score"]) + int(amount))
                break

        return self.find(user_input)

    def find(self, user_input):
        name = user_input.split()[1]
        result = []
        for row in self.tmp_db:
            if row.get("Name") == name:
                result.append(row)
                return result
                pass
            pass

        return [{'result':"There's no {}".format(name)}]

    def save(self, *args):
        f = open(self.db_name, "wb")
        pickle.dump(self.tmp_db, f)
        f.close()

    def run(self, user_input):
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
            return command[user_input.split()[0]](user_input)
        except KeyError:
            print("Please input correctly.")
            return "Please input correctly."


if __name__ == "__main__":
    db = Database("20171648-양기현-assignment3.dat")
    db.run()
