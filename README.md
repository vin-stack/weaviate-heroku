# Weaviate Heroku Project

This project demonstrates a basic setup of Weaviate on Heroku with functionalities like class creation, vector retrieval, and deletion.

## Setup

1. Ensure you have Docker and the Heroku CLI installed.
2. Log in to Heroku and create a new app:
   ```sh
   heroku login
   heroku create weaviate-database
   ```
3. Push the code to Heroku:
   ```sh
   git init
   git add .
   git commit -m "Initial Weaviate setup"
   git push heroku main
   ```

## Endpoints

- `POST /create` - Create an article with title, content, and vector.
- `GET /retrieve/<id>` - Retrieve an article by its ID.
- `DELETE /delete/<id>` - Delete an article by its ID.
