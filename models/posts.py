from engine.db_storage import DBStorage, freeudemydb
db = DBStorage()
posts = db.create_collection("posts")
post = { "post_title": "How to get a free udemy course", "post_author": "Adedayo Ayomide" }
posts.insert_one(post)