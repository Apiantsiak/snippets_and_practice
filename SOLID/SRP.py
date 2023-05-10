class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # Non SRP part

    # def save(self, filename):
    #     with open(filename, "w") as file:
    #         file.write(str(self))
    #
    # def losd(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


#  Part according to SRP

class PersistenceManager:

    @staticmethod
    def save_ro_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))
