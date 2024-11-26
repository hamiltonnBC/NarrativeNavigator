# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create instance directory if it doesn't exist
instance_path = os.path.join(basedir, 'instance')
Path(instance_path).mkdir(parents=True, exist_ok=True)

# Initialize Flask app with instance path
app = Flask(__name__, instance_path=instance_path)
CORS(app)

# Configure database with absolute path
db_path = os.path.join(instance_path, 'story.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200))

@app.route('/api/sections', methods=['GET'])
def get_sections():
    sections = Section.query.all()
    return jsonify([{
        'id': s.id,
        'title': s.title,
        'content': s.content,
        'tags': s.tags.split(',') if s.tags else []
    } for s in sections])

@app.route('/api/sections', methods=['POST'])
def create_section():
    data = request.json
    section = Section(
        title=data['title'],
        content=data['content'],
        tags=','.join(data.get('tags', []))
    )
    db.session.add(section)
    db.session.commit()
    return jsonify({
        'id': section.id,
        'title': section.title,
        'content': section.content,
        'tags': section.tags.split(',') if section.tags else []
    })

def init_db():
    with app.app_context():
        db.create_all()
        print(f"Database initialized at: {db_path}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)