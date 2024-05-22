from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

motor_speed = 0  # Global variable to store motor speed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_motor_speed', methods=['POST'])
def update_motor_speed():
    global motor_speed
    motor_speed = request.json['speed']
    print(motor_speed)
    return jsonify(status="success", motor_speed=motor_speed)

@app.route('/get_motor_speed', methods=['GET'])
def get_motor_speed():
    global motor_speed
    return jsonify(status="success", motor_speed=motor_speed)

@app.route('/power/<int:number>', methods=['GET'])
def power(number):
    result = number ** 2
    return jsonify(status="success", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
