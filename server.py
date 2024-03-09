from flask import Flask, render_template
app = Flask(__name__)

print("hello world")

@app.route('/')
def index():
    return  "Hello World"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4400, debug=True)
 
