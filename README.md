# api

[![ci](https://github.com/cstories-app/api/actions/workflows/ci.yml/badge.svg)](https://github.com/cstories-app/api/actions/workflows/ci.yml)

Source: [Using FastAPI to Build Python Web APIs – Real Python](https://realpython.com/fastapi-python-web-apis/)

Live at [https://api.cstories.app](https://api.cstories.app)

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
* docker

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

### Local Development

1. Clone the repo

    ```sh
    cd /share/github && \
    git clone https://github.com/cstories-app/api.git
    ```

1. Create `.env` file

    ```sh
    cd api && \
    echo "OPENAI_API_KEY=MY_KEY" >> .env
    echo "PATH_GOOGLE_SA_KEY_JSON=path/to/key.json" >> .env
    ```

1. Create the Python virtual environment

    ```sh
    python -m venv venv && \
    source venv/bin/activate
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
    ```

1. Run the app

    ```sh
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

1. Or use the [Dockerfile](./Dockerfile)

    ```sh
    docker run -it --rm -v $(pwd):/usr/local/app -v ${PATH_GOOGLE_SA_KEY_JSON}:/usr/local $(docker build -q -t fastapi .)
    ```

### Docker

[Install docs for Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

Run the Docker stack in daemon mode: `docker compose up -d`

### Apache

Create config: `/etc/apache/sites-available/api.conf`:

```apache
<VirtualHost *:80>
    ServerName api.cstories.app
    ServerSignature Off

    Header always unset X-Frame-Options
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header always set X-Content-Type-Options "nosniff"

    ErrorLog /var/log/apache2/redirect.error.log
    LogLevel warn

    ProxyPreserveHost On
    ProxyPass "/" "http://143.198.103.35:8000/"
    ProxyPassReverse "/" "http://143.198.103.35:8000/"

    #Redirect / https://api.cstories.app
    RewriteEngine on
    RewriteCond %{SERVER_NAME} =api.cstories.app
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName api.cstories.app
        ServerSignature Off

        Header always unset X-Frame-Options
        Header set X-Frame-Options "SAMEORIGIN"
        Header always set Strict-Transport-Security "max-age=63072000"
        Header set X-XSS-Protection "1; mode=block"
        Header always set X-Content-Type-Options "nosniff"

        ErrorLog /var/log/apache2/redirect.error.log
        LogLevel warn

        ProxyPreserveHost On
        ProxyPass "/" "http://143.198.103.35:8000/"
        ProxyPassReverse "/" "http://143.198.103.35:8000/"

        SSLCertificateFile /etc/letsencrypt/live/api.cstories.app/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/api.cstories.app/privkey.pem
        Include /etc/letsencrypt/options-ssl-apache.conf
    </VirtualHost>
</IfModule>
```

Create certs and enable the site:

```sh
sudo certbot certonly --apache
sudo a2ensite api.conf
sudo systemctl reload apache2
```
