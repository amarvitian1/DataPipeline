# DataPipeline

Steps :

Step 1: 
   Docker Image Creation :
      1. Used a base image of Python 3 , so that we can write the parsers and Etl component.
      2. Requirements we used , Pandas pymysql requests
            Pandas : For loading data to CSV , reading data from Sql Connections and performing Etl for change data capture.
            Requests : To Access the RSS url to download XML.
            Pymysql : To Access the Mysql Database.
Step 2 :
   Creation of Amazon RDS ( Mysql ).
   1. Reason for Selection of Mysql  : Since this was a small load of data , preferred to use relational database , but if we have to scale
   up , would have used Postgres MPP .
   2. Setup VPC groups to access the Mysql Database on AWS.  
   
   Mysql EndPoint : 
 
Step 3 :
   Creation of Etl Scripts :
     1. Ingester : To Ingest RSS XML to landing Folder.
     2. XMLParser : To Parse the incoming XML to Pandas Data Frame.( Also loaded to CSV for temporary Analysis)
     3. Load to Mysql : Performed the CDC operation and loaded to Mysql.( connectMySql)
     4. DataPipeline : Entry Point where it does all the 3 steps mentioned above.
    
Debug Steps to Run the Program Manually.
1. docker-compose build && docker-compose run --rm app bash\
2. python DataPipeline.py

Added the Setup for Notebook as a seperate Document in Git

            
            
