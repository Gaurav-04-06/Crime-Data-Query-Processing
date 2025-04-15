from flask import Flask, request, jsonify
from spark_processor import query_crime_data

app = Flask(__name__)

@app.route("/query", methods=["GET"])
def query():
    city = request.args.get("city")
    crime_code = request.args.get("crime_code")
    crime_type = request.args.get("crime_type")

    try:
        crime_code = int(crime_code) if crime_code else None
        result = query_crime_data(city, crime_code, crime_type)
        return jsonify({"status": "success", "data": result.to_json(orient="records")})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(port=5001)
