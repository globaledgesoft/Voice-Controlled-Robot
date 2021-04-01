import sys
import numpy as np

from std_msgs.msg import String
import rclpy
from rclpy.node import Node
from lex_common_msgs.srv import AudioTextConversation

rclpy.init()
node = rclpy.create_node('lex')
lex_service_name = "/lex_conversation"
lex_service = node.create_client(AudioTextConversation, lex_service_name)

# Process the audio request through lex and return response.
def handle_audio_input(request):
    audio_data = request
    accept_type = 'text/plain; charset=utf-8'
    lex_service_request = AudioTextConversation.Request()
    lex_service_request.content_type = 'audio/x-l16; sample-rate=16000; channel-count=1'
    lex_service_request.accept_type = accept_type
    lex_service_request.text_request = ''
    lex_service_request.audio_request = audio_data
    while not lex_service.wait_for_service(timeout_sec=1.0):
        print('service not available, waiting again...')
    lex_response = lex_service.call_async(lex_service_request)
    rclpy.spin_until_future_complete(node, lex_response)
    print("lex response",lex_response.result().text_response)
    return lex_response.result().text_response
