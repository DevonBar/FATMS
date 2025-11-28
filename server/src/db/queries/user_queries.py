def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, department,roles,shift_schedule FROM users")
    result = cursor.fetchall()
    cursor.close()
    return result


def create_user(conn, name, email):
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (name, email))
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    return last_id
