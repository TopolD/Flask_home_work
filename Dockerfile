FROM python:latest
EXPOSE 5000
WORKDIR /app
COPY  bib_list.txt ./

RUN pip install --no-cache-dir -r  bib_list.txt

COPY . .

CMD ["python", "New_breath.py"]
