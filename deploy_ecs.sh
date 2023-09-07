#!/bin/sh
export AWS_PROFILE=motionapp
echo "Deploying to DEV environmrnt"
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 451619694810.dkr.ecr.us-west-1.amazonaws.com
docker build -t fraud-check-service .
docker tag fraud-check-service:latest 451619694810.dkr.ecr.us-west-1.amazonaws.com/fraud-check-service:latest
docker push 451619694810.dkr.ecr.us-west-1.amazonaws.com/fraud-check-service:latest
#for taskarn in $(aws ecs list-tasks --cluster compaira-service-dev --service reports-service-dev --desired-status RUNNING --output text --query 'taskArns'); do aws ecs #stop-task --cluster compaira-service-dev --task $taskarn; done;
echo "DEV deployment completed"
