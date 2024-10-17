# [Django Dynamic Services](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html) 

Open-source **Django** project that showcases the **API Generator** and other **Dynamic Services** - actively supported by [App-Generator](https://app-generator.dev/).

- 👉 [Django - Build Services without Coding](https://www.youtube.com/watch?v=EtMCK5AmdQI) - `video presentation` (learn how to use this starter)

---

> For a **complete set of features** and long-term support, check out **[Dynamic Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)**, a powerful starter that incorporates:

- ✅ [Dynamic DataTables](https://app-generator.dev/docs/developer-tools/dynamic-django/datatables.html): using a single line of configuration, the data saved in any table is automatically managed
- ✅ [Dynamic API](https://app-generator.dev/docs/developer-tools/dynamic-django/api.html): any model can become a secure API Endpoint using DRF
- ✅ [Dynamic Charts](https://app-generator.dev/docs/developer-tools/dynamic-django/charts.html): extract relevant charts without coding all major types are supported
- ✅ [CSV Loader](https://app-generator.dev/docs/developer-tools/dynamic-django/csv-loader.html): translate CSV files into Django Models and (optional) load the information
- ✅ Powerful [CLI Tools](https://app-generator.dev/docs/developer-tools/dynamic-django/cli.html) for the GIT interface, configuration editing, updating the configuration and database (create models, migrate DB)

<br />

## Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`)

```bash
$ git clone https://github.com/app-generator/django-dynamic-services.git
$ cd django-dynamic-services
```

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.


> 👉 **Step 3** - Create Superuser in `Docker`

```bash
$ # List containes & get the ID
$ docker container ls  
$ # Create the superuser
$ docker exec <CONTAINER_ID> python manage.py createsuperuser 
```

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-dynamic-services.git
$ cd django-dynamic-services
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Generate API

```bash
$ python manage.py generate-api     # requires confirmation
// 
$ python manage.py generate-api -f  # no input (API folder is overwritten)
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/` and the generated API can be found at: 

- http://localhost:8000/api/product/ - For `products`
- http://localhost:8000/api/sales/ - For `sales` 

The default API nodes can be tested via this [POSTMAN](./media/test.postman_collection) Collection.  

<br />

## How to use the API

- Start the app
- Make sure the endpoints are up & running 
- Authenticate via API and het the access token
  - `http://localhost:8000/login/jwt/` usind existing credentials 
  - Save the token in the requests `HEADER`
- `GET Requests` are public (no token required)
  - GET ALL products: `http://localhost:8000/api/product/`
  - GET product by ID: `http://localhost:8000/api/product/1/`
  - GET ALL Sales: `http://localhost:8000/api/sales/`
- `Create`, `Delete`, `Update` requires a token in the header

For API sample requests, open and edit the [POSTMAN](./media/test.postman_collection) Collection sample.

<br />

## How Update the API

- Define or update your models
- Migrate the database
- Update the configuration `API_GENERATOR` section
- Regenerate the API
  - `python manage.py generate-api`

At this point, you should be able to use the API. For more information regarding the library used to generate the code, access: 

> 👉 [API Generator for Django](https://github.com/app-generator/django-api-generator) - Open-Source Library

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- includes                # 
   |              |-- footer.py          # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br /> 

---
[Django Dynamic Services](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html) - Open-Source **Django** starter provided by **[App-Generator](https://app-generator.dev/)**
