## Ml_project.
### Software and account Requirement.

1. [Github Account](https://git.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/download)
5. [GIT  Documentation](https://git-scm.com/docs/gittutorial)

creating conda environment
``` 
conda create -p venv python==3.7 -y
```

To activate environment
```
conda activate F:\Ineuron project\ml_project\venv
```

To activate environment
```
conda deactivate
```
command to install requirements is
``` 
pip install -r requirements.txt
```
.gitignore file is ignore the update of file in git
```
to add files to git 
```
git add . ##to add all file
```
or

git add <filename>
```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file\

To check the git status 
```
git status
```
To check all version maintained by git 
```
git log
```
To create version/commit all changes by git
```
git commit -m "massage"
```
To  send version/changes to github
```

git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = sagarkumar7788@gmail.com
2. HEROKU_API_KEY = b4dacf34-e50f-4ecf-b406-95deda12f962
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
> Note : Image name for docker must be lowercase

To list docker image 
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 55bfdc3e6549
```
>Note : -p stand for port number and -e for environment
```

To check running container in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
