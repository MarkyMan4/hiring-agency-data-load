with open('data/securityquestions.csv') as f:
    questions = f.readlines()
    questions = [q.replace('\n', '').replace("'", "''") for q in questions]

with open('sql/security_question_inserts.sql', 'w') as outfile:
    for q in questions:
        outfile.write(f"insert into agency_api_securityquestion (question) values (\'{q}\');\n")
