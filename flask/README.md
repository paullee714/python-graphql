# Flask - GraphQL 서버 만들기
- flask와 GraphQL 서버 만들기

## flask 환경 구성하기
### 가상환경 설정하기 (pipenv / virtualenv)
- pipenv 사용 할 경우
    ``` bash
    $ pip3 install pipenv 
    $ pipenv shell
    (venv) $ pipenv install flask
    ```
- virtualenv 사용 할 경우
    ```bash
    $ pip3 install virtualenv
    $ source venv/bin/activate
    (venv) $ pip3 install flask
    ```

### DB ORM 생성하기 
sqlacodegen mysql+pymysql://root:qwerqwer123@127.0.0.1:3306/employees>models.py