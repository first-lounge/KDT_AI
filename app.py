from flask import Flask, jsonify, request

jarvis = Flask(__name__)

@jarvis.route('/whoami')
def get_Id():
    return jsonify({"name" : "first-lounge"})

@jarvis.route('/echo')
def get_Echo():
    arg = request.args.get('string')
    return jsonify({"value" : arg})

weapon = {}
emp = "empty"
# Get -> read
@jarvis.route('/')
def get_weapon():
    if not weapon:
        return jsonify({'weapon_list': emp})
    return jsonify({'weapon_list': weapon})

# Post -> create
@jarvis.route('/', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    id = len(weapon) + 1
    weapon[id] = {
        "name" : request_data['name'],
        "stock" : request_data['stock']
    }

    return jsonify(weapon[id])

# Put -> update
@jarvis.route('/<int:id>', methods=['PUT'])
def update_weapon(id):
    request_data = request.get_json()
    try:
        weapon[id] = {"name" : request_data["name"], 
                      "stock" : request_data["stock"]
                      }
    except:
        return "Not In List"
    return jsonify(weapon[id])

# Delete -> delete
@jarvis.route('/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    try:
        del weapon[id]
    except:
        return "Not In List"

    return jsonify({'weapon_list': weapon})

if __name__ == '__main__':
    jarvis.run(debug=True)