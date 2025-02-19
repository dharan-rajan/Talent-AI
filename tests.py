from services import DBService
import re
import json

class DBTest:
    def test_query101(self):
        res = DBService("resumes").queryDocuments(["Reservation System"], 5)
        print(res)

    def test_jsonFetcher(self):
        res = " ... Wait, but I need to think about how to evaluate each component for this resume.\n\nFirstly, SM: How well do their skills match the job requirements. The job is about developing software solutions using various technologies like web-based tools and project management systems. The resume shows a wide range of technical skills in areas like JavaScript, XSL, Visual Basic, PHP, SQL, Mysql, LAMP, Photoshop, HTML, VBA, PHP, MySQL, etc.\n\nIn the job description, the primary focus is on software development using web-based solutions and project management tools. So their experience with web development (HTML, CSS) should be relevant.\n\nBut wait, in the resume, there's no experience with JavaScript or XSL for web development; instead, they have some experience in other languages, like Visual Basic and PHP. But these are related to database management, etc.\n\nHowever, since the job requires a strong knowledge of web development (HTML, CSS) which is somewhat covered by their experience with databases and such through Visual Basic? Or perhaps not directly.\n\nWait: They have an experience in Java-like programming, but no JavaScript or XSL. So maybe this is not as relevant as other areas. Hmm.\n\nAlso, the job involves project management, which requires knowledge of tools like LAMP, Mysql, etc., which are covered in their skills. But perhaps more crucially, they need experience with web technologies (like HTML, CSS) since the job is about developing software solutions using various technologies.\n\nAdditionally, there's significant experience in project management, particularly through roles as a Client Manager and Senior Production Associate, which would be relevant for understanding project lifecycle and managing multiple teams.\n\nSo SM: Maybe 6/10. They have some JavaScript and XSL but not strongly relevant to web development skills needed for the job.\n\nIR: The role is about developing software solutions using various technologies (web-based tools). Since their experience includes project management, which uses project management tools, they may be relevant here.\n\nEF: Education is from a US university with a degree in economics, minor in literature. Not sure how directly this ties to the IT industry or web development, but perhaps 7/10 as it's not technical.\n\nRE: Recent experience is limited—only up to two years in programming (JavaScript, XSL), one year project management, etc., and some involvement in client RFEs, product deployments. So RE score around 4/10.\n</think>\n\n```json\n{\n  \"SM\": \"6\",\n  \"YOE\": \"7\",\n  \"IR\": \"8\",\n  \"EF\": \"9\",\n  \"RE\": \"5\"\n}\n```"
        match = re.search(r'```json\n(.*?)\n```', res, re.DOTALL)
        json_str = match.group(1)
        data = json.loads(json_str)
        print(data)

DBTest().test_jsonFetcher()