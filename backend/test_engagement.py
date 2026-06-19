from db_connection import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    # Connection info
    cursor.execute("SELECT USER FROM dual")
    print("User:", cursor.fetchone()[0])

    cursor.execute("""
        SELECT SYS_CONTEXT('USERENV', 'DB_NAME'),
               SYS_CONTEXT('USERENV', 'CON_NAME')
        FROM dual
    """)

    db_name, con_name = cursor.fetchone()

    print("Database:", db_name)
    print("Container:", con_name)

    # Check table existence
    cursor.execute("""
        SELECT COUNT(*)
        FROM USER_TABLES
        WHERE TABLE_NAME = 'ENGAGEMENT_LOG'
    """)

    table_count = cursor.fetchone()[0]
    print("ENGAGEMENT_LOG Exists:", table_count)

    if table_count == 0:
        print("ERROR: ENGAGEMENT_LOG table not found!")
    else:
        # Test insert
        cursor.execute("""
            INSERT INTO ENGAGEMENT_LOG
            (STUDENT_ID, STATUS)
            VALUES (:1, :2)
        """, [1, "ATTENTIVE"])

        conn.commit()

        print("Test record inserted successfully.")

        # Verify insert
        cursor.execute("""
            SELECT LOG_ID, STUDENT_ID, STATUS
            FROM ENGAGEMENT_LOG
            ORDER BY LOG_ID DESC
            FETCH FIRST 1 ROWS ONLY
        """)

        row = cursor.fetchone()

        if row:
            print("Latest Record:")
            print(f"LOG_ID={row[0]}, STUDENT_ID={row[1]}, STATUS={row[2]}")

except Exception as e:
    print("Database Error:")
    print(e)

finally:
    try:
        cursor.close()
    except:
        pass

    try:
        conn.close()
    except:
        pass