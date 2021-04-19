from app import app
from config import Config
from midterms import init_midterm_members


with app.app_context():
    init_midterm_members(Config.MIDTERM_MEMBERS)
