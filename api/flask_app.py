from flask import Flask, request
import json

app = Flask(__name__)

link_dictionary = {
    1: 'https://drive.google.com/file/d/12_-dWmRyoVRfxI9u1LLeRVyJVdyERYzz/view?usp=drive_link',
    2: 'https://drive.google.com/file/d/1J2kHbVQ1uM3bScLIEuMQmkV__M-QOmin/view?usp=sharing',
    3: 'https://drive.google.com/file/d/1gGL3Wi51X0q4ysExntKVo7t-RqEzBH4h/view?usp=sharing',
    4: 'https://drive.google.com/file/d/17idxSG0-ZwTHE9a_zkEgCeuqSD_ziZ6M/view?usp=sharing',
    5: 'https://drive.google.com/file/d/1UVbgTLMcVjgEa0LZtb8F8nWdDwPnjx5O/view?usp=sharing',
    6: 'https://drive.google.com/file/d/1MhaYcaeVwhgGQhAdqZvdQ5H4e9UUYaF2/view?usp=sharing',
    7: 'https://drive.google.com/file/d/1GRZQwQwojk2jBXeZH5eIoQAY6BqT9UbT/view?usp=sharing',
    8: 'https://drive.google.com/file/d/1qhI1PpeGR8M-Ky-_5IJF_lt7XrK9zwOe/view?usp=sharing',
    9: 'https://drive.google.com/file/d/1EfBs3co1Zq0bSxSQDWrmZnRo_n3dTkRj/view?usp=sharing',
    10: 'https://drive.google.com/file/d/1EfBs3co1Zq0bSxSQDWrmZnRo_n3dTkRj/view?usp=sharing',
    11: 'https://drive.google.com/file/d/17tcFlmvBumdz2_0OscW0Bt8cP0_xnQ5A/view?usp=sharing',
    12: 'https://drive.google.com/file/d/1rir7Iovd3lYK7GaS-_KDVc7QZ5Xy1OIA/view?usp=sharing',
    13: 'https://drive.google.com/file/d/1TseDTon6wlB_Gzo6AYBQ1Mpejb9sMAWs/view?usp=sharing',
    14: 'https://drive.google.com/file/d/18GuBdGlVtC-275UFlG-kPUQeDzfkRco0/view?usp=sharing',
    15: 'https://drive.google.com/file/d/1u6RDKFp83YEWMGqWc4ZbCA1-AkcY0rsD/view?usp=sharing',
    16: 'https://drive.google.com/file/d/1_iCOXo2arFYPyNS7egrBzYllEGAYaY3h/view?usp=sharing',
    17: 'https://drive.google.com/file/d/1bdmIajQqB-cM0yUfuyqpj3QJslt_V0NZ/view?usp=sharing',
    18: 'https://drive.google.com/file/d/1zcZrEaYvPdu3bwwsUglfhwoMer2RDIE-/view?usp=sharing',
    19: 'https://drive.google.com/file/d/1x9p0DR0asGQ-lpv5qxVcYGsfZeZozflx/view?usp=sharing',
    20: 'https://drive.google.com/file/d/1k5NOMF6GxFMn9Ddaa7xGNaej1kMiT-z2/view?usp=sharing'
}
@app.route("/", methods = ['GET'])
def get_pic():
    number = int(str(request.args.get('input')))
    link = link_dictionary[number]
    user_data = {
        "link": link
    }
    json_dump = json.dumps(user_data)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True)