from flask import Flask, request
from steamship import Steamship
# from dotenv import load_dotenv
import os

# load_dotenv()

app = Flask(__name__)

workspace = os.environ.get('WORKSPACE')
steamship_plugin = os.environ.get('STEAMSHIP_PLUGIN')

client = Steamship(workspace=workspace)
generator = client.use_plugin(steamship_plugin)

@app.route('/')
def hello_world():
    return 'Hello, huxian99'

def test():
    print()

@app.route('/ai/gpt4')
def hello_user():
    # q = request.args.get('q')
    # task = generator.generate(text=q)
    # task.wait()
    # return task.output.blocks[0].text
    return 'hello'

if __name__ =="__main__":
    app.run(debug=True, port=8086)

