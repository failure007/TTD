FROM python:3.9

WORKDIR /

COPY . /test_sparse_recommender.py

CMD ["pytest", "test_sparse_recommender.py"]
