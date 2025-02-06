with app.app_context():
    db.drop_all()
    db.create_all()

    Ale = Students(name = "Alejandro Otermin", message = "Hi everyone, we'll be holding math tutoring after school in the gymtoday!")
    Yanis = Students(name = "Yanis Fellache", message = "Reminder basketball practice is today at 5:00")
    Stern = Admins(name = "Josh Stern", message = "Hey guys, reember the programming plans are due next Monday")
    Behar = Admins(name = "Marisa Behar", message = "Free snacks at programming comp today!")
    db.session.add(Ale)
    db.session.add(Yanis)
    db.session.add(Stern)
    db.session.add(Behar)
    db.session.commit()