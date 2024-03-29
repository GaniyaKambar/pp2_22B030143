import psycopg2
from config import config


def create_tables():
    """function to create user and user_score tables"""
    create_user_table_sql = """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(20) NOT NULL,
            user_data VARCHAR(40) NOT NULL
        );
    """
    create_user_score_table_sql = """
        CREATE TABLE user_scores (
            user_score_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            level INTEGER NOT NULL,
            user_score INTEGER NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
    """
    params = config()

    try:    
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(create_user_table_sql)
                cursor.execute(create_user_score_table_sql)
            connect.commit()
            print("Successfully created tables")
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not create tables: ", _ex)


def check_user_exists(user_name):
    """explicit function to check for the existance of the user in users table"""
    check_user_exists_sql = """
        SELECT COUNT(*) FROM users
        WHERE user_name = %s;
    """
    params = config()
    count = 0

    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(check_user_exists_sql, (user_name,))
                count = cursor.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not check the existence of the user: ", _ex)
    return count



def add_new_user(user_name):
    """function to add new user into users database, if it does not exist, 
        if exists, return the user information"""
    check_user_exists_sql = """
        SELECT COUNT(*) FROM users
        WHERE user_name = %s;
    """
    add_new_user_sql = """
        INSERT INTO users(user_name, user_data)
        VALUES (%s, %s);
    """
    params = config()
    isPresent = None
    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(check_user_exists_sql, (user_name,))
                isPresent = cursor.fetchone()[0]
                if isPresent == 0:
                    cursor.execute(add_new_user_sql, (user_name, f"{user_name}_data.txt"))
            connect.commit()
            print("Successfully added new user")
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not add the new user: ", _ex) 

def get_user_id(user_name):
    """function to get the user_if from the user_name"""
    get_user_id_sql = """
        SELECT user_id FROM users
        WHERE user_name = %s
    """
    params = config()
    user_id = None

    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(get_user_id_sql, (user_name,))
                user_id = cursor.fetchone()[0]
            connect.commit()
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not get the user_id: ", _ex)
    return user_id



def add_new_user_score(user_id, level, user_score):
    """function to add the new user_score into the user_score table"""
    check_user_score_exists_sql = """
        SELECT COUNT(*) FROM user_scores
        WHERE user_id = %s
    """

    add_new_user_score_sql = """
        INSERT INTO user_scores(user_id, level, user_score)
        VALUES (%s, %s, %s);
    """
    params = config()
    isPresent = None 

    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(check_user_score_exists_sql, (user_id,))
                isPresent = cursor.fetchone()[0]
                if isPresent == 0:
                    cursor.execute(add_new_user_score_sql, (user_id, level, user_score))
            connect.commit()
            print("Successfully added new user score")
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not add new user into the user_scores table: ", _ex)


def update_user_score(user_id, level, user_score):
    """function to update the current score of the user"""
    update_score_sql = """
        UPDATE user_scores
        SET level = %s,
            user_score = %s
        WHERE user_id = %s;
    """

    params = config()

    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(update_score_sql, (level, user_score, user_id))
            connect.commit()
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not update the user score: ", _ex)


def get_user_score(user_id):
    """function to get user score, level information from the table"""
    select_user_score_sql = """
        SELECT * FROM user_scores
        WHERE user_id = %s
    """

    params = config()
    user_score_info = None
    try:
        with psycopg2.connect(**params) as connect:
            with connect.cursor() as cursor:
                cursor.execute(select_user_score_sql, (user_id,))
                user_score_info = cursor.fetchone()[0]
            connect.commit()
    except (Exception, psycopg2.DatabaseError) as _ex:
        print("Could not get the user score information", _ex)

    return user_score_info












    

