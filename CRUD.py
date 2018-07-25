# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:58:45 2018

@author: Savira Hanandita
"""
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class User(Resource):
    
    
    def get(self,name):
        for user in user_review:
            if(name == user_review["id"]):
                return user, 200
        return "User not found,404"
    
    
    def post(self,name):
        parser = reqparse.Requestparser()
        parser.add_argument("order_id")
        parser.add_argument("product_id")
        parser.add_argument("user_id")
        parser.add_argument("rating")
        parser.add_argument("review")
        parser.add_argument("created_at")
        parser.add_argument("updated_at")
        args = parser.parse_args()
        
        for user in user_review:
            if(name == user["id"]):
                return "User with id {} already exists".format(name),400
        user = {
                "id" : name,
                "order_id" : args["order_id"],
                "product_id": args["product_id"],
                "user_id" : args["user_id"],
                "rating" : args ["rating"],
                "review" : args["review"],
                "created_at" : args["created_at"],
                "updated_at" : args["updated_at"]
                }
        user_review.append(user)
        return user,201
    
    
    def put(self,name):
        parser = reqparse.Requestparser()
        parser.add_argument("order_id")
        parser.add_argument("product_id")
        parser.add_argument("user_id")
        parser.add_argument("rating")
        parser.add_argument("review")
        parser.add_argument("created_at")
        parser.add_argument("updated_at")
        args = parser.parse_args()
        
        for user in user_review:
            if(name == user["id"]):
                "order_id" : args["order_id"]
                "product_id": args["product_id"]
                "user_id" : args["user_id"]
                "rating" : args ["rating"]
                "review" : args["review"]
                "created_at" : args["created_at"]
                "updated_at" : args["updated_at"]
                return user, 200
        
        user = {
                "id" : name,
                "order_id" : args["order_id"],
                "product_id": args["product_id"],
                "user_id" : args["user_id"],
                "rating" : args ["rating"],
                "review" : args["review"],
                "created_at" : args["created_at"],
                "updated_at" : args["updated_at"]
                }
        user_review.append(user)
        return user,201
                
    
    def delete(self,name):
        global user_review
        user_review= [user for user in user_review if user["id"] != name ]
        return "{} is deleted".format(name),200
        