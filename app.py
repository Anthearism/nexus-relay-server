from flask import Flask, request, jsonify
import time, random

app = Flask(__name__)
events = []

def clean(code):
    return "".join(c for c in str(code) if c.isdigit())[:10]

@app.route("/health")
def health():
    return jsonify({"ok": True})

@app.route("/register", methods=["POST"])
def register():
    return jsonify({"ok": True})

@app.route("/send", methods=["POST"])
def send():
    data = request.json or {}
    events.append(data)
    return jsonify({"ok": True})

@app.route("/poll")
def poll():
    code = clean(request.args.get("code", ""))
    found = []
    keep = []

    for e in events:
        if clean(e.get("to_code", "")) == code:
            found.append(e)
        else:
            keep.append(e)

    events[:] = keep
    return jsonify({"ok": True, "events": found})
