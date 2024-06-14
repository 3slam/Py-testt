from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_array():
    try:
        data = request.get_json()
        array = data['array']
        array_sum = sum(array)
        return jsonify({'sum': array_sum})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
