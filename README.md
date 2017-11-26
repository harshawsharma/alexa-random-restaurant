## alexa-random-restaurant

A basic python based backend for an Alexa skill that randomly gives you an open restaurant in a specified city using the Yelp API.


### Pre-requisites
- This project uses the latest [flask-ask](https://github.com/johnwheeler/flask-ask) code that supports directly invoking AWS Lambda (as opposed to invoking via API Gateway+Lambda)
- Create [Yelp App](https://www.yelp.com/developers/v3/manage_app). Client ID and Secret are required to make calls to Yelp

### The SAM template creates the following resources:
- 1 Lambda Function, python 2.7 with 2 environment variables(cliend id and secret)
- 1 IAM Role with 1 Managed Policy
- 1 Lambda Trigger, that allows Alexa Skills Kit to give permission to invoke Lambda

Once the SAM template is run to create these resources. Use the Lambda function's ARN and configure your [Alexa Skill](https://developer.amazon.com/edw/home.html)

### High level flow
Once set up, this would work as follows:

- When the following is asked 'Alexa, ask {skill name},  Pick a place for me in {city name}'
- Alexa, invokes the Lamdba function using the ARN configured
- The Lambda function is written in python using flask-ask. The function uses the lambda environment variables to communicate to yelp and obtain a list of restaurants for the city name provided. The call to yelp is configured to return only 10 open restaurants.
- The code then randomly picks one from the result set and returns a response back to Alexa to read out.


### Additional Considerations/Limitations

- Currently there is no validation of the city name provided
- The yelp call is hardcoded to return only 10 results

