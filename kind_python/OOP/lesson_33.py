class Women:
    title = "Class object for field title"
    photo = "Class object for field photo"
    ordering = "Class object for field ordering"

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            # self._t = Women.title


w = Women('root', '1234')

# print(w.ordering)
# print(w.Meta.ordering)
print(w.__dict__)
print()
print(w.meta.__dict__)