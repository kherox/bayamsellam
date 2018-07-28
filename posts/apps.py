from django.apps import AppConfig
import sys
from pprint import pprint

class PostsConfig(AppConfig):
    name = 'posts'




class PostMiddleware() :
    def __init__(self,get_response) :
        self.get_response = get_response
        self.current_user_id = None 
        
       
    def __call__(self,request) :
        user = getattr(request, "auth",None)
        self.get_current_user_id(request)
        response = self.get_response(request)
       
        return response
    
    def get_current_user_id(self,request) :
        self.current_user_id = request.user.id
        return self.current_user_id