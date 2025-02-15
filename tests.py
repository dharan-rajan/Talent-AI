from services import DBService

class DBTest:
    def test_query101(self):
        res = DBService("resumes").queryDocuments(["Reservation System"], 5)
        print(res)

DBTest().test_query101()