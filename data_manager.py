import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_first_last_names(cursor):
    cursor.execute("SELECT first_name, last_name FROM mentors;")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_miskolc_nicks(cursor, location):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = %(location)s;
                    """, {'location': location})
    nicks = cursor.fetchall()
    print(nicks)
    return nicks


@database_common.connection_handler
def get_carol_applicant_data(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name, phone_number FROM applicants
                    WHERE first_name = %(first_name)s;
                    """,{'first_name': first_name})
    carol_data = cursor.fetchall()
    return carol_data


@database_common.connection_handler
def get_hat_owner_applicant_data(cursor, email):
    cursor.execute("""
                    SELECT first_name, last_name, phone_number FROM applicants
                    WHERE email LIKE %(email)s;
                    """, {'email': email})
    hat_owners_data = cursor.fetchall()
    return hat_owners_data


@database_common.connection_handler
def insert_new_applicant(cursor, first_name, last_name, phone_number, email, application_code):

    # cursor.execute("""
    #                 INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
    #                 VALUES (%(first_name)s, %(last_name)s, %(phone_number)s, %(email)s, %(application_code)s);
    #                 """,
    #                {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number,
    #                 'email': email, 'application_code': application_code})

    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE application_code = %(application_code)s;
                    """,
                   {'application_code': application_code})
    new_applicant_data = cursor.fetchall()
    return  new_applicant_data


@database_common.connection_handler
def update_data(cursor, first_name, last_name, phone_number):
    cursor.execute("""
                    UPDATE applicants
                    SET phone_number = %(phone_number)s
                    WHERE first_name = %(first_name)s AND last_name = %(last_name)s
                    """,
                   {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number})
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE first_name = %(first_name)s AND last_name = %(last_name)s
                    """,
                   {'first_name': first_name, 'last_name': last_name})
    updated_data = cursor.fetchall()
    return updated_data


@database_common.connection_handler
def delete_applicants_mauriseu(cursor, email_domain):
    cursor.execute("""
                    DELETE FROM applicants
                    WHERE email LIKE %(email_domain)s;
                    """,
                   {'email_domain': email_domain})
    cursor.execute("""
                    SELECT * FROM applicants
                    """)
    remaining_applicants = cursor.fetchall()
    return remaining_applicants
