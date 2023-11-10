mamba create --prefix .\venv python=3.10
mamba activate .\venv\

python.exe -m pip install --upgrade pip
pip install -r requirements.txt
cd src/resources/
CALL npm i
cd..
cd..
