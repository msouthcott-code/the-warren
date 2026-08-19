import sqlite3

def generate_report(db_path):
    # Connection opened but never closed - resource leak
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT * FROM bunnies")
    rows = cursor.fetchall()
    
    # Silent failure - returns empty string instead of raising
    if not rows:
        return ""
    
    return "\n".join(f"{row[0]}: {row[1]} carrots" for row in rows)

def export_to_file(data, path):
    # No error handling around file write
    f = open(path, "w")
    f.write(data)
    # File never closed
