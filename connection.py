import pymongo


def db_connection():
    """Database connection"""

    conn_str = 'mongodb+srv://sherifsultan:3lgXfhp7vShrCqjz@cluster0.zhn66pq.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(conn_str)
    db = client["user_info"]
    collection = db["userinfo"]
    return collection