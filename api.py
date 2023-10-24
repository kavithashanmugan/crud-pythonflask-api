from flask import Flask, jsonify, request

app = Flask(__name__)

items = [{"id": 1,"name":"Item 1","description":"This is the first item."},{"id": 2,"name":"Item 2","description":"This is the second item."},{"id": 3,"name":"Item 3","description":"This is the third item."}]

# get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# get item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_byid(item_id):
    for item in items:
        if item['id']==item_id:
                if item is not None:
                     return jsonify(item)
                else:
                     return jsonify({"error": "Item not found"}), 404

# create new item
@app.route('/items', methods=['POST'])
def create_item():
     new_item={'id':len(items)+1,'name':request.json['name'],'description':request.json['description']}
     items.append(new_item)
     return jsonify(items)
     
#update new item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id): 
     for item in items:
            if item['id'] == item_id:
                 if item is not None:
                        updated_item={'id':item['id'],'name':request.json['name'],'description':request.json['description']}
                        return jsonify(updated_item)
                 else:
                     return jsonify({"error": "Item not updated"}), 404

     
#delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            return jsonify(items)

    return {"error": "Item with the given id not found"}, 404
                        
                 
if __name__ == '__main__':
    app.run(debug=True)