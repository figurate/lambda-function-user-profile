from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.integration import SNS
from diagrams.aws.network import APIGateway

with Diagram("User Profile", show=False, direction="TB"):

    userprofile = Lambda("user profile")
    # topic = SNS("user profile")

    APIGateway("user profile api") >> userprofile >> DynamodbTable("user profiles") >> userprofile
    # userprofile >> topic
