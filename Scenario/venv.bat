echo off 

set "DIR=PhoneBook"
mkdir "%DIR%"
pushd "%DIR%"

call exepoly.bat

python -m venv venv
call venv\Scripts\activate.bat

pip install psycopg2
pip freeze > requirements.txt

echo все готово
pause

