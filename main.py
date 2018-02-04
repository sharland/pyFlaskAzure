from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello azure - how are you doing today?'

if __name__ == '__main__':
  app.run()
