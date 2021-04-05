from flask_restful import Api, Resource, reqparse
from flask import after_this_request
import os
from api.TextBank import TextBank

text_bank = TextBank()

class ApiHandler(Resource):

  def __init__(self):
    print("initialising api handler")


  def get(self, lang):
    @after_this_request
    def after_request(response):
        text_bank.generate_more_text(lang)
        print("after_request")
        return response
    print('lang requested from api')
    print(lang)
    text = text_bank.get_text(lang)
    return {
      'resultStatus': 'SUCCESS',
      'message': text
      }

    

  def post(self, lang):
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)

    args = parser.parse_args()

    print(args)

    request_type = args['type']
    request_json = args['message']
    ret_status = request_type
    ret_msg = request_json

    if ret_msg:
      message = "Your Message Requested: {}".format(ret_msg)
    else:
      message = "No Msg"
    
    final_ret = {"status": "Success", "message": message}

    return final_ret