from flask import Flask, request
from steamship import Steamship
import os
# from dotenv import load_dotenv
# load_dotenv() 

app = Flask(__name__)

w = os.environ.get('WORKSPACE')
# p = os.environ.get('STEAMSHIP_PLUGIN')

@app.route('/')
def hello_world():
    return 'Hello, huxian99'

def test():
    print()

@app.route('/ai/gpt4')
def hello_user():
    try:
        client = Steamship(workspace=w)
        generator = client.use_plugin('gpt-4')
        q = request.args.get('q')
        task = generator.generate(text=q)
        task.wait()
        return task.output.blocks[0].text
    except Exception as e:
        return e
        

if __name__ =="__main__":
    app.run(debug=True, port=8086)

