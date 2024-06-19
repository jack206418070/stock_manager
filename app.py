from flask import Flask, render_template, jsonify, request, redirect, session, url_for
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import math, requests


app = Flask(
    __name__,
    static_folder='public',
    static_url_path='/'
)  # 建立 application 物件


CORS(app, resources={r"/api/*": {"origins": "*"}})
connection_string = "mongodb+srv://ginjack:a12081616@cluster0.js6ij.mongodb.net/"
client = MongoClient(connection_string)
app.secret_key = 'your_secret_key_here'
dbs = client.tools

# db_collection1 = 'test'
# db_collection2 = 'test_operation'

db_collection1 = 'appliance'
db_collection2 = 'operation'
# temp_data = [
#   {
#     "name": "刀片10號",
#     "initial_quantity": 200,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "刀片11號",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "刀片15號",
#     "initial_quantity": 200,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD注射針頭18號",
#     "initial_quantity": 600,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD注射針頭21號",
#     "initial_quantity": 600,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD注射針頭25號",
#     "initial_quantity": 300,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD注射針頭27號(3/4長針)",
#     "initial_quantity": 200,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD注射針頭30號",
#     "initial_quantity": 400,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD心肌長針23號(7mm)",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 1ml螺旋空針",
#     "initial_quantity": 100,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 3ml一般空針",
#     "initial_quantity": 400,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 3ml螺旋空針",
#     "initial_quantity": 0,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 5ml一般空針",
#     "initial_quantity": 400,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 5ml螺旋空針",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "terumo10ml螺旋空針",
#     "initial_quantity": 300,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD20ml一般空針",
#     "initial_quantity": 120,
#     "current_quantity": 239,
#     "unit_quantity": 120
#   },
#   {
#     "name": "BD20ml螺旋空針",
#     "initial_quantity": 192,
#     "current_quantity": 191,
#     "unit_quantity": 48
#   },
#   {
#     "name": "BD50ml一般空針",
#     "initial_quantity": 50,
#     "current_quantity": 49,
#     "unit_quantity": 50
#   },
#   {
#     "name": "BD50ml螺旋空針",
#     "initial_quantity": 120,
#     "current_quantity": 239,
#     "unit_quantity": 60
#   },
#   {
#     "name": "BD 0.3ml胰島素空針",
#     "initial_quantity": 300,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 0.5ml胰島素空針",
#     "initial_quantity": 300,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "BD 1ml胰島素空針",
#     "initial_quantity": 200,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "普惠灌食空針",
#     "initial_quantity": 50,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "灌腸管18Fr",
#     "initial_quantity": 20,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "雙叉導尿管14Fr",
#     "initial_quantity": 5,
#     "current_quantity": 19,
#     "unit_quantity": 10
#   },
#   {
#     "name": "單導管",
#     "initial_quantity": 20,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "導尿包",
#     "initial_quantity": 20,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "尿袋",
#     "initial_quantity": 2,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "滅菌揚克式抽吸管",
#     "initial_quantity": 30,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋外科接管Suction tube(360cm)",
#     "initial_quantity": 50,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "太平洋傷口引流瓶/胸腔引流瓶",
#     "initial_quantity": 9,
#     "current_quantity": 4,
#     "unit_quantity": 1
#   },
#   {
#     "name": "無止溢閥廢液收集軟袋",
#     "initial_quantity": 50,
#     "current_quantity": 49,
#     "unit_quantity": 50
#   },
#   {
#     "name": "有止溢閥廢液收集軟袋",
#     "initial_quantity": 0,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "5mm penrose",
#     "initial_quantity": 0,
#     "current_quantity": 50,
#     "unit_quantity": 50
#   },
#   {
#     "name": "太平洋全矽質全凹槽圓管10Fr(穿刺針)",
#     "initial_quantity": 6,
#     "current_quantity": 9,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋全矽質全凹槽圓管15Fr(穿刺針)",
#     "initial_quantity": 12,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋7mm矽質扁管",
#     "initial_quantity": 8,
#     "current_quantity": 9,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋7mm矽質扁管(穿刺針)",
#     "initial_quantity": 2,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋10mm矽質扁管",
#     "initial_quantity": 20,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "太平洋真空引流球125ml",
#     "initial_quantity": 50,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "50ml小燈籠",
#     "initial_quantity": 4,
#     "current_quantity": 3,
#     "unit_quantity": 1
#   },
#   {
#     "name": "越聖拋棄式電極板",
#     "initial_quantity": 100,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "電刀清潔片",
#     "initial_quantity": 80,
#     "current_quantity": 29,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-中衛滅菌2X2紗布不織布",
#     "initial_quantity": 200,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛滅菌2X2Y型不織布紗布",
#     "initial_quantity": 200,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛未滅菌2X2磅裝紗布",
#     "initial_quantity": 200,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛滅菌3X3紗布",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛滅菌4X4紗布",
#     "initial_quantity": 100,
#     "current_quantity": 199,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛X光顯影紗布-腹部墊(30cmX30cm,5pcs)",
#     "initial_quantity": 0,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛阻力線紗布(10cmX10cm,10pcs)",
#     "initial_quantity": 200,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-中衛醫療用棉墊(12.5X20cm,2pcs)",
#     "initial_quantity": 75,
#     "current_quantity": 149,
#     "unit_quantity": 75
#   },
#   {
#     "name": "健陽-中衛醫療用棉墊(20X30cm,1pcs)",
#     "initial_quantity": 20,
#     "current_quantity": 29,
#     "unit_quantity": 10
#   },
#   {
#     "name": "健陽-未滅菌大棉球",
#     "initial_quantity": 1,
#     "current_quantity": 2,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-ENT止血棉(2*6cm,5pcs)",
#     "initial_quantity": 9,
#     "current_quantity": 4,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-滅菌ENT止血棉條",
#     "initial_quantity": 15,
#     "current_quantity": 19,
#     "unit_quantity": 5
#   },
#   {
#     "name": "健陽-2吋平面消毒管袋",
#     "initial_quantity": 2,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-3吋平面消毒管袋",
#     "initial_quantity": 1,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-4吋平面消毒管袋",
#     "initial_quantity": 1,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-6吋立體消毒管袋",
#     "initial_quantity": 2,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-8吋立體消毒管袋",
#     "initial_quantity": 1,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-1/2吋高壓滅菌貼紙",
#     "initial_quantity": 2,
#     "current_quantity": 0,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-1吋高壓滅菌貼紙",
#     "initial_quantity": 5,
#     "current_quantity": 2,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-高壓消毒滅菌指示劑",
#     "initial_quantity": 2,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-20ml 生理食鹽水",
#     "initial_quantity": 600,
#     "current_quantity": 499,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-30ml水溶性優碘",
#     "initial_quantity": 30,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-450ml水溶性優碘",
#     "initial_quantity": 3,
#     "current_quantity": 4,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-OPA",
#     "initial_quantity": 2,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-中衛拋棄式無菌刷手服",
#     "initial_quantity": 10,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-未滅菌隔離衣",
#     "initial_quantity": 20,
#     "current_quantity": 9,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-不織布帽",
#     "initial_quantity": 0,
#     "current_quantity": 4,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-鞋套",
#     "initial_quantity": 0,
#     "current_quantity": 2,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-3吋滅菌小棉棒",
#     "initial_quantity": 50,
#     "current_quantity": 299,
#     "unit_quantity": 50
#   },
#   {
#     "name": "健陽-6吋滅菌普通棉棒",
#     "initial_quantity": 300,
#     "current_quantity": 299,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-滅菌ENT棉棒",
#     "initial_quantity": 50,
#     "current_quantity": 19,
#     "unit_quantity": 10
#   },
#   {
#     "name": "健陽-滅菌沖洗棉棒",
#     "initial_quantity": 150,
#     "current_quantity": 299,
#     "unit_quantity": 50
#   },
#   {
#     "name": "健陽-Jetstar手術記號筆(一字平胸用)",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "健陽-3Mtegaderm+pad (5cm*7cm)",
#     "initial_quantity": 100,
#     "current_quantity": 149,
#     "unit_quantity": 50
#   },
#   {
#     "name": "健陽-免縫膠帶(12*100mm)",
#     "initial_quantity": 350,
#     "current_quantity": 249,
#     "unit_quantity": 50
#   },
#   {
#     "name": "健陽-免縫膠帶(25*125mm)",
#     "initial_quantity": 100,
#     "current_quantity": 124,
#     "unit_quantity": 25
#   },
#   {
#     "name": "健陽-2吋自黏彈繃",
#     "initial_quantity": 20,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-6吋彈性繃帶",
#     "initial_quantity": 18,
#     "current_quantity": 59,
#     "unit_quantity": 6
#   },
#   {
#     "name": "健陽-6吋彈性紗捲",
#     "initial_quantity": 12,
#     "current_quantity": 29,
#     "unit_quantity": 6
#   },
#   {
#     "name": "健陽-3M 半吋膚色紙膠",
#     "initial_quantity": 48,
#     "current_quantity": 23,
#     "unit_quantity": 6
#   },
#   {
#     "name": "健陽-3M 1吋膚色紙膠",
#     "initial_quantity": 24,
#     "current_quantity": 11,
#     "unit_quantity": 6
#   },
#   {
#     "name": "健陽-3M 2吋通氣膠帶",
#     "initial_quantity": 0,
#     "current_quantity": 1,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-黏布膠",
#     "initial_quantity": 4,
#     "current_quantity": 4,
#     "unit_quantity": 1
#   },
#   {
#     "name": "健陽-皮膚縫合釘",
#     "initial_quantity": 54,
#     "current_quantity": 41,
#     "unit_quantity": 6
#   },
#   {
#     "name": "健陽-內視鏡保護套",
#     "initial_quantity": 100,
#     "current_quantity": 99,
#     "unit_quantity": 100
#   },
#   {
#     "name": "捷揚-擠乳袋",
#     "initial_quantity": 10,
#     "current_quantity": 19,
#     "unit_quantity": 1
#   }
# ]
# print(len(temp_data))
# for doc in temp_data:
#   dbs[db_collection1].insert_one(doc)


@app.before_request
def check_admin():
    if request.endpoint == 'login' or request.endpoint == 'error_500' or request.endpoint == 'logout':
        return None
    if 'display_name' not in session or session['display_name'] != '管理員':
        return redirect(url_for('login'))


@app.route('/500')
def error_500():
    return render_template('500.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    data = request.form
    user = dbs.user.find_one({"$and": [{"account": data['account']}, {"password": data['password']}]})
    if user:
      session['display_name'] = user['display_name']
      session['name'] = user['name']
      return redirect('/')
    else:
      return redirect(url_for('login'))
  
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('login'))

@app.route('/getData')
def getData():
  data = []
  temp_data = dbs[db_collection1].find({})
  for doc in temp_data:
    del doc['_id']
    status = doc.get('status', 0)
    if doc['current_quantity'] >= doc['initial_quantity'] or status == 2:
      need_add = math.ceil((doc['current_quantity'] + 1 - doc['initial_quantity']) / doc['unit_quantity'])
      if not doc.get('unit', None):
        doc['unit'] = '盒'
        if doc['unit_quantity'] == 1:
          doc['unit'] = '個'
      if need_add < 0:
        need_add = 0
      doc['need'] = need_add
      doc['status'] = doc.get('status', 1)

      if doc['status'] != 2 and need_add > 0:
        doc['status'] = 1
      data.append(doc)
    else:
      if not doc.get('unit', None):
        doc['unit'] = '盒'
        if doc['unit_quantity'] == 1:
          doc['unit'] = '個'
      doc['need'] = 0
      doc['status'] = 0
      data.append(doc)
  return jsonify({"data": data}), 200


@app.route('/comfrim_order', methods=['POST'])
def comfrim_order():
  json_data = request.get_json()
  for doc in json_data:
    dbs[db_collection1].update_one({"name": doc['name']}, {"$set": {"status": 2, "add_tools": doc['add_tools'], "add_date": doc['add_date']}})
  return jsonify({"status": "success"}), 200


@app.route('/write_off', methods=['POST'])
def write_off():
  json_data = request.get_json()
  total_number = json_data['add_tools']
  temp_count = json_data.get('temp_count', 0)
  all_count = 0
  print(json_data)
  for doc in json_data['writeOff_data']:
    print(doc)
    total_number= total_number - doc['write_count']
    all_count += doc['write_count']
  print(total_number)
  if total_number == 0:
    status = 0
    json_data['writeOff_data'] = []
    json_data['add_date'] = ""
    json_data['add_tools'] = 0
    json_data['temp_count'] = 0
    temp_count = 0
  else:
    status = 2
    temp_count += (all_count - temp_count)
  json_data['initial_quantity'] += json_data['unit_quantity'] * (all_count - temp_count) 
  dbs[db_collection1].update_one({"name":json_data['name']}, {"$set": {"status": status, "writeOff_data": json_data['writeOff_data'], "add_date": json_data['add_date'], "add_tools": json_data['add_tools'], "initial_quantity": json_data['initial_quantity'], "temp_count": temp_count}})
  return jsonify({"status": "success"}), 200

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/tool_setting', methods=['POST', 'GET'])
def tool_setting():
  tools_data = []
  if request.method == 'POST':
    json_data = request.get_json()
    if json_data['methods'] == 'edit':
      dbs[db_collection1].update_one({"name": json_data['old_name']}, {"$set": {"initial_quantity": json_data['initial_quantity'], "current_quantity": json_data['current_quantity'], "name": json_data['name'], "unit": json_data['unit']}})
      if json_data['old_name'] != json_data['name']:
        temp_operation = dbs[db_collection2].find({})
        for doc in temp_operation:
          for idx, op_data in enumerate(doc['instruments']):
            if op_data['name'] == json_data['old_name']:
              dbs[db_collection2].update_one({"name": doc['name']}, {"$set": {f"instruments.{str(idx)}.name": json_data['name']}})
    elif json_data['methods'] == 'delete':
      print(json_data['name'])
      dbs[db_collection1].delete_one({"name": json_data['name']})
      temp_operation = dbs[db_collection2].find({})
      for doc in temp_operation:
        for idx, op_data in enumerate(doc['instruments']):
          if op_data['name'] == json_data['name']:
            print('in same')
            dbs[db_collection2].update_one({"name": doc['name']},{"$pull": {"instruments": {"name": json_data['name']}}})
    else:
      del json_data['methods']
      dbs[db_collection1].insert_one(json_data)

  temp_data = dbs[db_collection1].find({})
  for doc in temp_data:
    del doc['_id']
    if doc['current_quantity'] >= doc['initial_quantity']:
      if not doc.get('unit', None):
        doc['unit'] = '盒'
        if doc['unit_quantity'] == 1:
          doc['unit'] = '個'
      tools_data.append(doc)
    else:
      if not doc.get('unit', None):
        doc['unit'] = '盒'
        if doc['unit_quantity'] == 1:
          doc['unit'] = '個'
      tools_data.append(doc)
  return jsonify({"data": tools_data}), 200

@app.route('/get_toolName')
def get_toolName():
  tool_name = []
  temp_data = dbs[db_collection1].find({})
  for idx, doc in enumerate(temp_data):
    tool_name.append({
      "id": idx + 1,
      "name": doc['name']
    })
  return jsonify({"data": tool_name})

@app.route('/tool_page')
def tool_page():
  return render_template('tools_setting.html')

@app.route('/send_message', methods=['POST'])
def send_message():
  json_data = request.get_json()['message']
  requests.post('https://notify-api.line.me/api/notify', headers={'Authorization': 'Bearer OOPWSvfHppeiKWHosCnwqmJi2U7pJIWYFTAB556diP5'}, data={"message": json_data})
  return jsonify({})

@app.route('/operation_page')
def operation_page():
  return render_template('operation_page.html')


@app.route('/get_operation')
def get_operation():
  operation_data = []
  temp_data = dbs[db_collection2].find({})
  for doc in temp_data:
    del doc['_id']
    operation_data.append(doc)
  return jsonify({"data": operation_data})

@app.route('/create_operation', methods=['POST'])
def create_operation():
  json_data = request.get_json()
  data = dbs[db_collection2].find_one({"name": json_data['name']})
  if data == None:
    dbs[db_collection2].insert_one({"name": json_data['name'], "instruments": []})
  return jsonify({})


@app.route('/operation_setting', methods=['POST'])
def operation_setting():
  json_data = request.get_json()
  dbs[db_collection2].update_one({"name": json_data['name']}, {"$set": {"instruments": json_data['instruments']}})
  return jsonify({})


@app.route('/operation_sub_tools', methods=['POST'])
def operation_sub_tools():
  json_data = request.get_json()
  sub_list = []
  op_count = json_data['count']
  op_data = dbs[db_collection2].find_one({"name": json_data['name']})

  for doc in op_data['instruments']:
    sub_list.append(
      {
        "name": doc['name'],
        "count": int(doc['quantity']) * int(op_count)
      }
    )

  for doc in sub_list:
    current_quantity = dbs[db_collection1].find_one({"name": doc['name']}, {"initial_quantity": 1})
    if current_quantity:
      new_quantity = current_quantity['initial_quantity'] - doc['count']
      if new_quantity < 0:
          new_quantity = 0
      dbs[db_collection1].update_one({"name": doc['name']}, {"$set": {"initial_quantity": new_quantity}})
  
  return jsonify({})
  

@app.route('/update_operation_name', methods=['POST'])
def update_operation_name():
  json_data = request.get_json()
  dbs[db_collection2].update_one({'name': json_data['old_name']}, {"$set": {"name": json_data['new_name']}})
  return jsonify({}), 200


if __name__ == '__main__':
  app.run(port=5088)