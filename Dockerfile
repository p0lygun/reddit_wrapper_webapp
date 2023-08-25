# build stage
FROM python:3.11-buster as builder


# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY backend/ /project/backend

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm install --prod --no-self --no-lock --no-editable


FROM node:latest as node_base
RUN echo "NODE Version:" && node --version
RUN echo "NPM Version:" && npm --version

COPY frontend/ /frontend
WORKDIR /frontend
RUN npm install
RUN npm run ci

# run stage
FROM python:3.11-buster as final

RUN rm -rf /var/lib/apt/lists/*
# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs
# retrieve executables
COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/
COPY --from=node_base /frontend/src /project/frontend/

COPY backend/ /project/backend
WORKDIR /project
