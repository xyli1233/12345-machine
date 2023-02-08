from flask import Flask
from flask import jsonify
app = Flask(__name__)

def cal(start, end, num):
    if num <=1:
        return [{'sum':-99999999)}]
    sum = (start + end)*num/2
    return [{'sum':sum}]


@app.route('/')
def hello():
    print("I am an Arithmetic Progression Sum Calculator")
    return 'Hello Arithmetic Progression Sum Calculator! Please use it to calculate the sum at route by typing: /start/end/num'

@app.route('/<start>/<end>/<num>')
def changeroute(start, end, num):
    print(f"Solved for start:{start} and end:{end} and num:{num}")

    result = cal(float(start), float(end), int(num))
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
