from flask import Flask , jsonify

friend_list = [ 

    {
        "name":"Rahul",
        "age":42,
        "profession":'Trainer',
        "location":"remote"
    },


    {
        "name":"Ujjwal",
        "age":40,
        "profession":'Credit Analyst',
        "location":"Abu Dhabi"
    },
    
    {
        "name":"Jyotish",
        "age":25,
        "profession":'Analyst',
        "location":"Bangalore"
    },


]

# Create End points 

# https://127.0.0.1:5000/all ---> GET request 


app = Flask(__name__)

@app.route('/all',methods=["POST","GET"])
def get_friend_list():
    return jsonify({"friends":friend_list})



@app.route('/<name>')                    # http://127.0.0.1:5000/rahul
def get_particular_friend(name):
    for friend in friend_list:
        if friend['name'] == name:
            return jsonify(friend)
        else:
            return jsonify({"message":"friend not found"})


app.run(debug=True)

