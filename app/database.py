"""Defines all the functions related to the database"""
from app import db


def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from userInfo;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:

        item = {
            "user_id": result[0],
            "location": result[1],
            "test_status": result[2],
            "vaccine_status": result[3]
        }


        todo_list.append(item)

    return todo_list

def fetch_search(search_keyword:str) -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()

    print(search_keyword)

    query = 'SELECT * FROM userInfo WHERE location= "{}";'.format(search_keyword)

    query_results = conn.execute(query).fetchall()
    print(query_results)
    todo_list = []
    for result in query_results:

        item = {
            "user_id": result[0],
            "location": result[1],
            "test_status": result[2],
            "vaccine_status": result[3]
        }

        todo_list.append(item)

    conn.close()
    return todo_list

def fetch_advanced() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()

    query = 'select userInfo.user_id, subquery.city, subquery.country, subquery.avg_new_cases from (select cities.city AS city, avg(new_cases) AS "avg_new_cases", covid.location AS country from covid join cities on covid.location = cities.country group by city) AS subquery join userInfo on subquery.city = userInfo.location order by userInfo.user_id LIMIT 15'

    query_results = conn.execute(query).fetchall()
    print(query_results)
    todo_list = []
    for result in query_results:

        item = {
            "user_id": result[0],
            "city": result[1],
            "country": result[2],
            "avg_new_cases": result[3]
        }
        todo_list.append(item)

    conn.close()
    return todo_list

def update_task_entry(text: str) -> None:
    """Updates task description based on given `user_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """
    print("updated")
    split_text = text.split(",")

    conn = db.connect()
    query = 'Update userInfo set location= "{}", test_status = "{}", vaccine_status= "{}" where user_id = "{}";'.format(split_text[1], split_text[2], split_text[3], split_text[0])
    results = conn.execute(query)
    print(results)
    conn.close()


def update_status_entry(user_id: str, text: str) -> None:
    """Updates task status based on given `user_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
        """
    return None
    # conn = db.connect()
    # query = 'Update userInfo set status = "{}" where user_id = \'{}\'';'.format(text, user_id)
    # conn.execute(query)
    # conn.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    #parse text to get the values. The text must be in the form of comma separated values
    split_text = text.split(",")

    if len(split_text) != 4:
        print("add failure: format error")
        return

    conn = db.connect()
    query = 'Insert Into userInfo (user_id,location,test_status,vaccine_status) VALUES ("{}", "{}", "{}", "{}");'.format(
        split_text[0], split_text[1], split_text[2], split_text[3])
    conn.execute(query)
    # query_results = conn.execute("Select LAST_INSERT_ID();")
    # query_results = [x for x in query_results]
    # task_id = query_results[0][0]
    conn.close()

    return None

def remove_task_by_id(user_id: str) -> None:
    """ remove entries based on user ID """
    conn = db.connect()
    query = 'Delete From userInfo where user_id=\'{}\';'.format(user_id)
    conn.execute(query)
    conn.close()
