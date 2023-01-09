FROM continuumio/miniconda3

RUN conda install -y -c conda-forge \
    pillow \
    fastapi \
    uvicorn \
    python-multipart

RUN pip install numpy
RUN pip install sklearn

COPY kaggle_titanic_model.pkl ./kaggle_titanic_model.pkl
COPY main.py ./main.py

CMD uvicorn main:app --host=0.0.0.0 --port=$PORT