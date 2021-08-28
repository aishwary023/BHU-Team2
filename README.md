# BHU-Team2
![screencapture-localhost-8080-2021-08-28-15_53_21](https://user-images.githubusercontent.com/26626415/131214840-a5573e06-a4d1-47bf-9f74-d31bc81f1128.png)


## Frontend
**Stack** - VueJS
**Description** - A progressive web application, which queries the backend server to fetch OHCL data for a time interval. Charts are displayed using ```chart.js```

Install dependencies using:
```
npm install
```
Run the app using:

```
npm run serve
```

## Backend
![screencapture-127-0-0-1-8000-stock-list-2021-08-28-15_55_55](https://user-images.githubusercontent.com/26626415/131214909-96d3cbb7-4f4a-48f1-a96b-ad2108e7d3ee.png)

**Stack** - Django Rest Framework
### API Endpoints
- ```/tock/create``` - To create objects for stocks in the database
- ```/stock/list``` - to query stocks by using queryparams (```symbol```, ```start```, ```end```)

### Setting up the project

- Make sure `python3.7` and `pip` are installed. Install `pipenv` by running `pip install pipenv`.
- Install python dependencies using the command `pipenv install` Please use only pipenv for managing dependencies (Follow this [link](https://realpython.com/pipenv-guide/) if you are new to pipenv).
- To activate this project's virtualenv, run `pipenv shell`.
- Run `python manage.py migrate` to apply migrations.
- Start the development server using `python manage.py runserver`
- Open ```Postman``` and send a ```POST``` request with the JSON data as body to  [http://127.0.0.1:8000/stock/create](http://127.0.0.1:8000/stock/create).
- Once the data is added to the database, we can use the Frontend Application.