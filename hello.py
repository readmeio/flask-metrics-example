from flask import Flask
from readme_metrics import MetricsApiConfig, MetricsMiddleware

app = Flask(__name__)

# Docs: https://docs.readme.com/developers/docs/authentication#api-key-quick-start
README_API_KEY="YOUR_API_KEY"

app.wsgi_app = MetricsMiddleware(
    app.wsgi_app,
    MetricsApiConfig(
        README_API_KEY,
        lambda req: {
            'id': 'owlbert',
            'label': 'Owlbert',
            'email': 'owlbert@readme.io'
        },
        buffer_length=1, # makes it so logs show up after each request, rather than after each batch of 10
    )
)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'