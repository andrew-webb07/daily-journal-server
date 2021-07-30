class Entry:
    def __init__(self, id, date, concept, journal_entry, mood_id):
        self.id = id
        self.date = date
        self.concept = concept
        self.journal_entry = journal_entry
        self.mood_id = mood_id
        self.mood = None
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)