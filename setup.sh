#!/bin/bash

# Create main project directory
mkdir story-tracker
cd story-tracker

# Create backend structure
mkdir -p backend/{models,routes,instance}
touch backend/__init__.py
touch backend/app.py
touch backend/requirements.txt
touch backend/models/{__init__.py,models.py}
touch backend/routes/{__init__.py,api.py}

# Create requirements.txt content
cat > backend/requirements.txt << EOL
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-CORS==3.0.10
python-dotenv==0.19.0
EOL

# Initialize git repository
git init

# Create .gitignore
cat > .gitignore << EOL
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
*.db

# React
node_modules/
/build
.env.local
.env.development.local
.env.test.local
.env.production.local
npm-debug.log*
yarn-debug.log*
yarn-error.log*
EOL

echo "Basic structure created!"