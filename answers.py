num_users = 29

with open('sql/answer_inserts.sql', 'w') as outfile:
    for i in range(num_users):
        user_id = i + 1

        outfile.write(f"insert into agency_api_securityquestionanswer (answer, question_id, user_id) values ('blue', 2, {user_id});\n")
        outfile.write(f"insert into agency_api_securityquestionanswer (answer, question_id, user_id) values ('yetti', 7, {user_id});\n")
        outfile.write(f"insert into agency_api_securityquestionanswer (answer, question_id, user_id) values ('coffee', 15, {user_id});\n")
