<!-- echo "# Student_Maths" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/maheshpachpande/Student_Maths.git
git push -u origin main -->


->git remote add origin https://github.com/maheshpachpande/Student_Maths.git
->git branch -M main
->git push -u origin main

conda create -p student_venv python=3.8 -y

conda activate C:\Users\Mahesh\Desktop\student_maths\student_venv

or

conda activate student_venv/


import dagshub
dagshub.init(repo_owner='pachpandemahesh300', repo_name='mlproject_student', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)