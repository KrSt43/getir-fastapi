# getir-fastapi
HOW to START THE PROJECT

After cloning the project create an environment with,
python -m venv env
After creating the environment you have to create a .env file in root folder.
.env file has to have postgresql info on there like the example down below
SQLALCHEMY_DATABASE_URL = 'postgre-url-here'
After creating .env and creating virtual environment activate the virtual environment with,
source env/Scripts/activate
After activating the virtual environment you have to download requirements with,
pip install -r requirements.txt
After the requirements finished you can start the project with
uvicorn Driver.main:app --reload
