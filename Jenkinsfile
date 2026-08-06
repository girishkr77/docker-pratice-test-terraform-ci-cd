pipeline{
agent any
environment {
AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
}
stages{
stage('git push'){
steps{
sh 'mkdir -p build_room && cd build_room && echo "FROM alpine:latest" > Dockerfile'
sh 'docker build -t my-first-container:v1 build_room'
}
}
stage('python integration'){
steps{
sh 'aws ecr get-login-password --region ap-south-1|docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com'
sh 'docker tag my-first-container:v1 arn:aws:ecr:ap-south-1:${AWS_ACCOUNT_ID}:repository/django:latest'
sh 'docker push arn:aws:ecr:ap-south-1:${AWS_ACCOUNT_ID}:repository/django:latest'
}
}
}
}
