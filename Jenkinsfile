pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        PYTHON_PATH = 'C:\\Users\\royba\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}\\${VIRTUAL_ENV}")) {
                        bat "\"${env.PYTHON_PATH}\" -m venv ${VIRTUAL_ENV}"
                    }
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && pip install -r requirements.txt && pip install coverage"
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && flake8 myapp/app.py"
                }
            }
        }
        stage('Security') {
            steps {
                script {
                    
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && bandit -r myapp/"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && set PYTHONPATH=%CD% && pytest"
                }
            }
        }

        stage('Coverage') {
            steps {
                script {
                    // Run tests with coverage and show report in console
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && coverage run -m pytest"
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && coverage report"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
