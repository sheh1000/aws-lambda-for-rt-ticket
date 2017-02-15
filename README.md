# aws-lambda-for-rt-ticket
**Description** 

This is a AWS lambda function to process alerts from New Relic and create ticket in Request Tracker using RT API. 
You can invoke a Lambda function over HTTPS. You can do this by defining a custom REST API and endpoint using Amazon API Gateway. When New Relic send an HTTPS request to the API endpoint, the Amazon API Gateway service invokes the corresponding Lambda function.

Example article: https://framework.realtime.co/blog/using-webhooks-in-aws-lambda.html

**Tips** 



Use https://github.com/nficano/python-lambda project to deploy Lambda function to AWS




**Troubleshooting** 

If you got the error 

    "ImportError: No module named rtapi" 
    
then just copy __rtapi.py__ to __/root/.virtualenvs/pylambda/local/lib/python2.7/site-packages/__
    
before you ran __'lambda deploy'__ command
