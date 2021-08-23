"""Application entry point."""
from project import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', ssl_context='adhoc')
