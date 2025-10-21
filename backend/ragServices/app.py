from flask import Flask,request,jsonify
from retriever import getAnswer

app = Flask(__name__)

@app.route("/ask",methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")
    answer = getAnswer(query)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
