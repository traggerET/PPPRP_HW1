from flask import Flask
import datetime

app = Flask(__name__)
cnt = 0

@app.route('/time', methods=['GET'])
def get_time():
    global cnt
    cnt += 1
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/statistics', methods=['GET'])
def get_stats():
    global cnt
    return str(cnt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
