from flask import Flask, request, jsonfy
from google.cloud import firestore
import datetime

app = Flask(__name__)
db = firestore.Client()

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/notes', methods=['GET'])
def get_notes():
    notes_ref = db.collection('notes')
    docs = notes_ref.stream()

    notes = []
    for doc in docs:
        notes.append(doc.to_dict())

    return jsonfy(notes)

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json

    note = {
        "message": data.get("message")
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "version": 1
    }

    db.collection('notes').app(note)

    return {"message": "note added"}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    