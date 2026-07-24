import json
import ollama
from datetime import datetime

today = datetime.now()
# from dotenv import load_dotenv

# load_dotenv()

# take in text from m3mmo.py as the message
def parse_reminder(text):

    # create a response object
    response = ollama.chat(
        # select model, max tokens and send messages to the model for action
        # in this case we do not need a conversation history, just the one-way transaction

        # return what was extracted from the message as a JSON file matching the database rows in Reminders from m3mmory.db
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": f"""Extract reminder details from this message and return ONLY valid JSON, no other text.

Message: "{text}"

Return this exact shape:
{{
  "type": "use 'appointment' if it has a specific date and time or the word appointment in the prompt, use 'reminder' for general reminders or anything else.",
  "title": "concise 2-4 word label for the appointment, e.g. 'VA Medical Appointment', 'Dentist Checkup', 'Car Service'",
  "name": "name of person the appointment is for, options will be Taylor, Lexy, Layna, or Avery. Null if no names mentioned.",
  "date": "date in friendly format like 'July 24th, 2026', assume current year is {today.year} if no year mentioned, or null",
  "time": "time in 12hr format like 4:00PM or 4:30PM, or null",
  "location": "if no location is mentioned is null. if 'VA' is mentioned use the Conroe VA Hospital.",
  "complete": 0
}}"""
            }
        ]
    )

    raw = response['message']['content']



    result = json.loads(raw)

    for key, value in result.items():
        if value == "null":
            result[key] = None

    return result



if __name__ == "__main__":
    result = parse_reminder("remind me about my VA appiontment on August 5th at 4PM")
    print(result)