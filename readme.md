# Utils AI Plugin

This repository contains Utils AI Plugin (a Quart-based API application providing various utility endpoints). It's designed to be run in a Docker container and is equipped with an NGINX configuration for reverse proxy setup.

## Features

- Base64 Encoding/Decoding
- URL Encoding/Decoding
- MD5 and SHA256 Hash Generation
- UUID Generation
- Color Code Conversion (HEX to RGB and vice versa)
- Timestamp Conversion
- JWT Token Generation and Verification
- Static file serving from `static/` directory
- Serving `legal.txt` content on `/legal` endpoint

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- NGINX (for reverse proxy setup)
- Make (optional for using the Makefile)

### Installing

1. **Clone the Repository**

   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. ** Build the Docker Image **

Use the provided Makefile:

``` 
make build
```

Or directly with Docker:

```
docker build -t [app-name] .
```

3. **Run the Docker Container**

Using the Makefile:

```
make run
```
Or using Docker:

```
docker run -d -p 5000:5000 --name [app-name] [app-name]
```

4. **Set Up NGINX Reverse Proxy (Optional)**

Modify the provided NGINX configuration file as needed and move it to the appropriate directory. You can use the Makefile to do this:

```
make install
```

### Usage

Access the API endpoints at http://localhost:5000/. The available endpoints are:

- /base64?data=[data]&action=[encode/decode]
- /url?data=[data]&action=[encode/decode]
- /md5?data=[data]
- /sha256?data=[data]
- /uuid
- /color-conversion?color=[color-code]&format=[hex/rgb]
- /timestamp-conversion?timestamp=[unix-timestamp]&format=[date-format]
- /jwt-generate?JWT_SECRET=[your-secret]
- /jwt-verify?JWT_SECRET=[your-secret]
- /legal

### Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

### Authors

- Emre Yilmaz - prompter
- ChatGPT - v4 - initial coding 

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.
