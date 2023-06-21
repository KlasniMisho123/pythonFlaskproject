from flaskblog import app, db

if __name__ == "__main__":
    with app.app_context() as r:
        from flaskblog.models import User, Post

        db.create_all()
        # print(User.query.all())

    app.run(debug=True)

# orjer rato shveba/ lupavs
# instanceshi rato ikmneba site.db

"""        #db.create_all()
        #user_1 = User(username="Yoruichi", email="ok.2@gmail.com", password="password2")
        #user_2 = User(username="Fubuki", email="ok.3@gmail.com", password="password3")

        #user = User.query.get(3)
        # post_1 = Post(title="Blog 1", content="First Post Content!", user_id=user.id)
        # post_2 = Post(title="Blog 2", content="Second Post Content!", user_id=user.id)

        #for post in user.posts:
            #post = post.query.first()
            # author_id = user.id
            #print(post)
            #print(post.author.username)
            # print(user.query.get(author_id))

        #db.session.commit()

        # print(user.id)
        #db.drop_all()
        """
