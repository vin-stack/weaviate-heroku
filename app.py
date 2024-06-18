import weaviate
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Use authentication credentials from environment variables
auth_credentials = (os.getenv('WEAVIATE_AUTHENTICATION_ADMIN_USERNAME'), os.getenv('WEAVIATE_AUTHENTICATION_ADMIN_PASSWORD'))
client = weaviate.Client("http://weaviate:8080", auth_client_secret=auth_credentials)

# Ensure the Weaviate schema exists
def ensure_schema():
    class_obj = {
        "class": "Article",
        "description": "A collection of articles",
        "properties": [
            {
                "name": "title",
                "dataType": ["string"],
                "description": "The title of the article"
            },
            {
                "name": "content",
                "dataType": ["string"],
                "description": "The content of the article"
            },
            {
                "name": "vector",
                "dataType": ["blob"],
                "description": "The vector representation of the article"
            }
        ]
    }
    client.schema.create_class(class_obj)

@app.route('/create', methods=['POST'])
def create_article():
    data = request.json
    client.data_object.create(
        data_object={
            "title": data["title"],
            "content": data["content"],
            "vector": data["vector"]
        },
        class_name="Article"
    )
    return jsonify({"status": "created"}), 201

@app.route('/retrieve/<id>', methods=['GET'])
def retrieve_article(id):
    article = client.data_object.get_by_id(id)
    if article:
        return jsonify(article)
    return jsonify({"error": "Article not found"}), 404

@app.route('/delete/<id>', methods=['DELETE'])
def delete_article(id):
    client.data_object.delete(id)
    return jsonify({"status": "deleted"}), 204

if __name__ == '__main__':
    ensure_schema()
    app.run(host='0.0.0.0', port=8080)
