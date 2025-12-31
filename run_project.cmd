@echo off

:: 1. Kiem tra va cai dat thu vien
python -m pip install -r requirements.txt

:: 2. Chay notebook Preprocess
python -m nbconvert --to notebook --execute app/preprocess.ipynb --output-dir=app/

:: 3. Chay notebook Train
python -m nbconvert --to notebook --execute app/Train.ipynb --output-dir=app/

:: 4. Don dep file tam va chay Streamlit
if exist app\*.nbconvert.ipynb del /q app\*.nbconvert.ipynb
python -m streamlit run demo/demo.py

pause