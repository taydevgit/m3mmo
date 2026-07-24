from wr4ngler import parse_reminder
from datetime import datetime

def handle_reminder(conn, cur, text):
    # take in a cursor object and the text itself
    parts = text.split(" ")
    command = parts[0][1:]

    if(text.startswith("!")):
        match command:
            case"appointments":
                rows = cur.execute("SELECT id, name, title, date, time, location FROM reminders").fetchall()
                if not rows:
                    return "No appointments found."
                response = "**Appointments:**\n"
                for row in rows:
                    date = datetime.strptime(row[3], "%Y-%m-%d").strftime("%B %d")
                    response += f"`[{row[0]}]` {row[2]} — {row[1]} — {date} at {row[4]}"
                    if row[5]:
                        response += f" @ {row[5]}"
                    response += "\n"
            
                return response

            case"next":
                row = cur.execute("SELECT id, name, title, date, time, location FROM reminders WHERE complete=0 ORDER BY date ASC LIMIT 1").fetchone()
                if not row:
                    return "No upcoming appointments."

                date = datetime.strptime(row[3], "%Y-%m-%d").strftime("%B %d")
                response = f"**Next appointment:** {row[2]} — {row[1]} — {date} at {row[4]}"
                if row[5]:
                    response += f" @ {row[5]}"
                
                return response

            case"delete":
                if len(parts) < 2:
                    return "Usage: !delete <id>"
                reminder_id = parts[1]
                cur.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
                return f"Reminder `{reminder_id}` deleted."

            case"reschedule":
                if len(parts) < 3:
                    return "Usage: !reschedule <id> <new date>"
                reminder_id = parts[1]
                new_date = parts[2]
                cur.execute("UPDATE reminders SET date=? WHERE id=?", (new_date, reminder_id))
                return f"Reminder `{reminder_id}` rescheduled to {new_date}."

            case _:
                return "Unrecognized command."
    else:
        data = parse_reminder(text)
        cur.execute("""INSERT INTO reminders (type, title, name, date, time, location, complete)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (data['type'], data['title'], data['name'], data['date'], data['time'], data['location'], 0))
        conn.commit()
        return f"Got it! Added: **{data['title']}** for {data['name'] or 'anyone'} on {data['date']} at {data['time']}."