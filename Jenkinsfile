pipeline{
agent any
environment {
AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
}
stages{
stage('terraform script'){
steps{
sh 'terraform init'
sh 'terraform plan'
sh 'terraform apply --auto-approve'
}
}
stage('human intervention'){
steps{
input_message : 'vpc grid is avaliable need to destroy',ok:'approve destroy'
}
}
stage('terraform destroy'){
steps {
sh 'terraform destroy --auto-approve'
}
}
}
}
