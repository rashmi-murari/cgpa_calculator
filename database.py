import sqlite3
from encryption import encrypt_text, decrypt_text


def save_to_database(name, reg, tgpa1, tgpa2, cgpa):
    """Saves the TGPA and CGPA data to the SQLite database."""
    name_enc = encrypt_text(name)
    reg_enc = encrypt_text(reg)

    conn = sqlite3.connect('mysql.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO result(name, id, tgpa1, tgpa2, cgpa) VALUES(?,?,?,?,?)',
            (name_enc, reg_enc, tgpa1, tgpa2, cgpa)
        )
        conn.commit()


def fetch_from_database(search_id):
    """Fetches student record from the SQLite database using student ID."""
    search_id_enc = encrypt_text(search_id)
    conn = sqlite3.connect('mysql.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM result WHERE id = ?', (search_id_enc,))
    result = cursor.fetchone()

    if result:
        name_dec = decrypt_text(result[0])
        id_dec = decrypt_text(result[1])
        return name_dec, id_dec, result[2], result[3], result[4]
    return None
