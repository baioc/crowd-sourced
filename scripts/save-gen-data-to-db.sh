cd server
echo "$PWD"
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mongo_insertion.py