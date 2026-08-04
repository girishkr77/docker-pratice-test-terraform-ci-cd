pipeline{
agent any

stages{
stage('git push'){
steps{
sh 'ls -la'
}
}
stage('python integration'){
steps{
sh 'docker --version'
sh 'terraform --version'
}
}
}
}
