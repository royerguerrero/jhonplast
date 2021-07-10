# JhonPlast Website
## Requirements
- Python3
- Pip3
- MongoDB Server
## How run the project
1. Create a virtual enviroment `python3 -m venv .env` and activate `source .env/bin/activate`
2. Install flask and more dependences `pip3 install -r requirements.txt` 
3. Expose the needed env variables
    - `expose FLASK_APP=main`
    - `expose FLASK_ENV=development`
4. Run `flask run`