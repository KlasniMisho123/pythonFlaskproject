from flaskblog import app, db

if __name__ == "__main__":
    with app.app_context() as r:
        from flaskblog.models import User, Post

        #db.create_all()
        # print(User.query.all())
        # db.drop_all()
        # db.session.commit()

    app.run(debug=True)





