from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("Web Service", show=False, outformat="png", filename="diagram"):
    ELB("lb") >> EC2("web") >> RDS("db")
