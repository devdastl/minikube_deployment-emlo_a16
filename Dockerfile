FROM zironycho/pytorch:1120-cpu-py38

WORKDIR /opt/src

COPY src/requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt \
	&& rm -rf /root/.cache/pip

WORKDIR /app
COPY src/ .

EXPOSE 7860

CMD ["uvicorn", "api_server:app", "--reload", "--port", "7860", "--host", "0.0.0.0"]