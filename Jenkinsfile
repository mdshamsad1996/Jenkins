pipeline {
	
    stages {
		stage('stage 1 -Install Dependencies'){
			steps{
				sh 'pip install -r requirements.txt'
			}
		}
        stage('Stage 2 - Check Python version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Stage 3 - Run get_capital_of_country Api') {
            steps {
                sh 'python src/get_capital_of_country.py'
            }
        }
		stage('Stage 4- Run unittest case of App'){
			steps {
				sh 'python -m unittest tests/test_get_capital_of_country.py'
			}
		}
    }
}