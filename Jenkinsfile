pipeline{
agent any
environment {
AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
}
stages{
stage('docker') {
steps {
sh 'docker build -t my-first-container:v2 build_room'
sh 'aws ecr get-login-password --region ap-south-1|docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com'
sh 'docker tag my-first-container:v2 185188589995.dkr.ecr.ap-south-1.amazonaws.com/django:v2'
sh 'docker push 185188589995.dkr.ecr.ap-south-1.amazonaws.com/django:v2'
}
}
stage('terraform script'){
steps{
sh 'terraform init'
sh 'terraform plan'
sh 'terraform apply --auto-approve'
}
}
stage('human intervention'){
steps{
input message: 'vpc grid is avaliable need to destroy',ok:'approve destroy'
}
}
stage('terraform destroy'){
steps {
sh 'terraform destroy --auto-approve'
}
}
}
}
