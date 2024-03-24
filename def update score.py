def quiz_history(username):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quiz_attempts WHERE username = ?", (username,))
    attempts = cursor.fetchall()
    print("Quiz History:")
    for attempt in attempts:
        print(f"Date: {attempt[1]}, Category: {attempt[2]}, Score: {attempt[3]}/{attempt[4]}")
    conn.close()
