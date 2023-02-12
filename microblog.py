
from app import app, db
from app.models import User, Content, UserHistory

@app.shell_context_processor
def make_shell_context():
    return {'UserHistory': UserHistory}