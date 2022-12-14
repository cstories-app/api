# api

Source: [Using FastAPI to Build Python Web APIs – Real Python](https://realpython.com/fastapi-python-web-apis/)

## Server

* $12/month
* Ubuntu 22.04 LTS x64
* 2 GB RAM  |  1 CPU  |  50GB SSD
* Region: sfo3
* Hostname: `cstories`
* IP: `164.92.110.38`

### Users

* bbest
* cgrant
* jzadra

`sudo usermod -a -G sudo <user>`

### Packages

#### apt

* net-tools
* python-is-python3
* python3.10-venv
* apache2

#### snap

* certbot

### Share

1. Add users to common group

    ```sh
    sudo usermod -g staff <user>
    ```

1. Make shared directory

    ```sh
    sudo mkdir -p /share/github
    ```

1. Change group of shared directory and set permissions

    ```sh
    sudo chgrp -R staff /share && \
    sudo chmod -R 2774 /share && \  # inherit, read, write, execute
    ```

## API

1. Clone the repo

    ```sh
    cd /share/github && \
    git clone https://github.com/cstories-app/api.git
    ```

1. Create `.env` file

    ```sh
    cd api && \
    echo "OPENAI_API_KEY=MY_KEY" >> .env
    ```

1. Create the Python virtual environment

    ```sh
    python -m venv venv && \
    source venv/bin/activate
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
    ```

1. Open firewall at port 8000 (**for development only**)

    ```sh
    sudo ufw allow 8000
    ```

1. Run the app

    ```sh
    uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
    ```

1. See it live: [http://164.92.110.38:8000](http://164.92.110.38:8000)
