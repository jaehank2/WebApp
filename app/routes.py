""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

search_items = None
advanced_items = None

@app.route("/delete/<string:user_id>", methods=['POST'])
def delete(user_id):
    """ recieved post requests for entry delete """
    try:
        db_helper.remove_task_by_id(user_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit", methods=['POST'])
def update():
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    print("received request \n")

    data = request.get_json()
    
    if data['description'] == "advanced":
        print("this is advanced query")
        items = db_helper.fetch_advanced()
        global advanced_items
        advanced_items = items
        result = {'success': True, 'response': 'Done'}
        return jsonify(result)       

    #If the input is just a search keyword
    if len((data['description'].split(","))) == 1:
        print("this is a search query")
        items = db_helper.fetch_search(data['description'])
        global search_items
        search_items = items
        result = {'success': True, 'response': 'Done'}
        return jsonify(result) 
    
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    print("homepage \n")
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)



@app.route("/search")
def search():
    print("search \n")
    """ returns rendered homepage """
    return render_template("index.html", items=search_items)

@app.route("/advanced")
def advanced():
    print("advanced \n")
    """ returns rendered homepage """
    return render_template("advanced_index.html", items=advanced_items)