# Degressly Demo

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/daniyaalk)

---

## What is this?

A one-click docker compose deployment for the entire degressly stack, along with a sample application for illustration.

## What do I need to run this?

1. [Docker Runtime](https://www.docker.com/get-started/)
2. [Docker Compose Plugin](https://docs.docker.com/compose/install/)
3. [MongoDB Compass](https://www.mongodb.com/try/download/compass) (Optional)


## How does the demo application work?

It's a single API application that runs on different ports corresponding to the type of application replica;
    
    1. 8080: Primary
    2. 8081: Secondary
    3. 8082: Candidate

The application returns a fixed XML response along with calling the postman echo API (http://postman-echo.com).

There are some fields which are consistent across all three of the replicas, and some fields with self descriptive names and values that are supposed to illustrate a regression in the code.

## How do I try this?

1. Clone all repositories 
```
git clone https://github.com/degressly/degressly-core.git
git clone https://github.com/degressly/degressly-comparator.git
git clone https://github.com/degressly/degressly-downstream.git
git clone https://github.com/degressly/degressly-demo.git
```

2. Build all images
```
cd degressly-demo
docker compose build . # For Linux, Windows
docker-compose build . # For Macos
```

3. Run the stack
```
docker compose up -d # For Linux, Windows
docker-compose up -d # For Macos
```

4. Make a request on http://localhost:8000 (Port exposed by the degressly proxy container)

5. Check the differences in response and downstream API calls

```
docker logs -f degressly-comparator
```

If you wish to get a visual representation, you can connect to the mongo instance to see the report as GUI:

Connect to MongoDB Instance using the following connection string:

```
mongodb://degressly_user:secure_password@localhost:27017/
```

Open the database named `degressly`, then open the collecion named `traceDocument`.


