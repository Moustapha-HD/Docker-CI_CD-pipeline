# Docker - CI/CD Pipeline

## Overview
CI/CD pipeline using Docker for testing an API. The API uses a sentiment analysis algorithm to predict whether a sentence has a positive or negative character. API entry points:
* `/status` returns 1 if the API works fine
* `/permissions` returns a user's permissions
* `/v1/sentiment` returns the sentiment analysis (-1 is negative, +1 is positive) using an old model
* `/v2/sentiment` returns the sentiment analysis using a new model

Three tests to do:
1) Authentication : To verify that the identification logic is working properly
2) Authorization : To verify that the logic for managing the user's access rights is working correctly
3) Content : To verify that the API works as expected
 
## How to use
`cd my_docker_authentification`
`docker image build . -t authentification_image:latest`

`cd ../my_docker_authorization` 
`docker image build . -t authorization_image:latest`

`cd ../my_docker_content` 
`docker image build . -t content_image:latest`

`docker-compose up`

## Example

```
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username=alice
    | password=wonderland

    expected result = 200
    actual restult = 200

    ==>  SUCCESS

    ============================
        Authorization test
    ============================

    request done at "v1/sentiment"
    | username=alice
    | password=wonderland

    expected result = 200
    actual restult = 200

    ==>  SUCCESS

    ============================
        Content test
    ============================

    request done at "v1/sentiment"
    | username=alice
    | password=wonderland

    expected result = 200
    actual restult = 200

    ==>  SUCCESS

    ==> Score =  0.5994

```
