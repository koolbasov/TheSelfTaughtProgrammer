class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self._unsafe = "опасно"

    def public_method(self):
        # клиенты могу это использовать
        pass

    def _unsafe_mthod(self):
        # клиенты не должны это использовать
        pass
        self.public = "безопасно"
        self._unsafe = "опасно"
