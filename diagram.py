from diagrams import Diagram
from diagrams.aws.compute import Lambda

with Diagram("Python Function Template", show=False, direction="TB"):

    Lambda("python function")
