# Admission_prediction





Creating virtual environment in your project folder
```
conda create -p myenv python=3.10 -y

```
Activate the environment created

```
conda activate myenv/

pip install -r requirements.txt

```

To check docker version 
```
dockers --version

````

To build docker we use

```
docker build .

```

To give the name to the docker tag we use

```
docker build . -t <tag_name>

```

We must follow this heirarcy

```
FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python app.py

```

We check the docker images we use

```
docker images

```

#To push your image to docker hub

we must login to docker hub

```
docker login

```

After login we follow

```

docker tag <repository_name>:<version> <username>/<repository_name> 
docker push <username>/<repository_name>
wait for the upload

```

To pull docker image we follow

```

docker pull <user_name>/<repository_name>

```

# **You can run this project using Dockers image**

You can pull the docker image and run it in the docker container using the following command in your terminal
```
docker pull zeeshankhan29/adm_predict
```