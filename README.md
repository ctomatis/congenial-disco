# Congenial disco

### Installation

***Congenial disco*** requires Python 3.8+ to run.

Get the git checkout of ***Congenial disco*** package in a new virtualenv and run in development mode.

```sh
$ git clone https://github.com/ctomatis/congenial-disco.git
$ cd congenial-disco
$ python3 -m venv .env
$ . .env/bin/activate
(.env)$ pip install .
```

Or just clone this repository, build and then run the Dockerize app (see below).

```sh
$ git clone https://github.com/ctomatis/congenial-disco.git
$ cd congenial-disco
```

### Configuration
Configure [AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-set) environment variables.

#### Virtualenv
The example below show how you can configure env variables in Linux.
```sh
$ export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
$ export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
$ export AWS_REGION=us-east-1
```

#### Docker
In the ***Dockerfile***, assign the value to each AWS environment variable.

```docker
...
ENV AWS_REGION=us-east-1
ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
...
```

### Run
#### Virtualenv
```sh
(.env)$ python main.py
# ----------------------------------------
# (required) Please enter your name: Cristian
# (required) Please enter your email: ctomatis@gmail.com
# (optional - defaults to txns.csv) Please enter CSV filename (fullpath): 
# ----------------------------------------
```

#### Docker
```sh
# Build the image.
$ docker build -t app .
# Run container.
$ docker run --rm -v $(pwd)/txns.csv:/app/txns.csv --name container app Cristian ctomatis@gmail.com
```
