class Ship:

    def __init__(self, draft, crew):

        self.draft = draft
        self.crew = crew

    def is_worth_it(self):

        sum_crew = self.crew * 1.5

        difference = self.draft - sum_crew

        if difference > 20:
            return True
        else:
            return False




        