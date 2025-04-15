from app import db, app
from app.models import User, Post


app_context = app.app_context()
app_context.push()
u1 = User(username='kitson', email='kitson@example.com')
u1.set_password("kitson")
db.session.add(u1)
p1 = Post(body='a', author=u1)
p2 = Post(body='b', author=u1)
p3 = Post(body='c', author=u1)
p4 = Post(body='d', author=u1)
p5 = Post(body='e', author=u1)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.commit()
