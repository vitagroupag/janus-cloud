FROM python:3.9
WORKDIR /app/
COPY . ./janus-cloud
RUN pip install --use-feature=in-tree-build /app/janus-cloud