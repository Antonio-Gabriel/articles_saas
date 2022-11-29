
<h1 align="center">Articles Application</h1>

<span align="center">

![Fastapi](https://img.shields.io/badge/fastapi-6DA55F?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%23007ACC.svg?style=for-the-badge&logo=docker&logoColor=white)
![Rocketry](https://img.shields.io/badge/rocketry-black?style=for-the-badge&logo=rocketry%20web%20tokens)
![Pytest](https://img.shields.io/badge/Pyttest-%23404d59.svg?style=for-the-badge&logo=pytest&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-%23316192.svg?style=for-the-badge&logo=python&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

</span>

<h4 align="center"> 
	🚧  Articles 🚀 Under construction...  🚧
</h4> 

<hr />

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">Author</a> &#xa0; | &#xa0;  
</p>

<br>

## :dart: About ##

The articles app is an application that shows information related to space travel based on `Space Flight News which` is a public api with this information.

It's is a challenge by [Codesh](https://coodesh.com/).

## :sparkles: Features ##

- [x] Create articles
- [x] Update articles by id
- [x] Filter article by id
- [x] Show all articles
- [x] Pagination on articles list
- [x] Validation on payloads to create and update article
- [x] Task Scheduled to run daily at 9h
- [x] Docker added to download postgres image and build the application
- [x] Migrations schema

## :rocket: Technologies ##

The following tools were used in this project:

- [Python: 3.10](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Rocketry](https://rocketry.readthedocs.io/en/stable/)
- [Fastapi](https://fastapi.tiangolo.com/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pylint](https://pylint.pycqa.org/en/latest/)
- [Pre-commit](https://pre-commit.com/)
- [Autopep8](https://pypi.org/project/autopep8/#installation)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python: 3.10](https://www.python.org/) and [Docker](https://www.docker.com/) installed.

After rename `env.example` file to `env`

<b>Note:</b> You really need to install docker if you don't have.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/Antonio-Gabriel/articles_saas

# Access
$ cd articles_saas

# Build the application
$ sudo docker-compose up --build

# The server will initialize in the <http://0.0.0.0:8001>
```

If any error occurred you can check on log:

[Logs file](src/application/security/logs/logs.log)

Endpoint for see the documentation

- `[GET]/docs:` the documentation of project

## :memo: Author ##

Made with :heart: by <a href="https://github.com/Antonio-Gabriel" target="_blank">António Gabriel</a>
