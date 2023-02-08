from flask import Flask
from flask import jsonify
app = Flask(__name__)

def chicken_rabbit_cage(heads, legs):
    for rabbit in range(heads + 1):
        chicken = heads - rabbit
        if 2 * chicken + 4 * rabbit == legs:
            return [{'chicken':chicken}, {'rabbit':rabbit}]
    return [{'chicken':-1}, {'rabbit':-1}]


@app.route('/')
def hello():
    print("I am an Automatic chicken_rabbit_cage problem solving Machine")
    return 'Hello Automatic chicken_rabbit_cage problem solving Machine! Please use it to solve chicken-rabbit-cage problem at route by typing: /chicken_rabbit_cage/x/y (x is heads and y is legs)'

@app.route('/chicken_rabbit_cage/<heads>/<legs>')
def changeroute(heads, legs):
    print(f"Solve chicken_rabbit_problems for heads:{heads} and legs:{legs}")

    result = chicken_rabbit_cage(int(heads), int(legs))
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
