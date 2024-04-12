import os # for os functions
import sys # for system functions
import json # for parsing strings
import smtplib, ssl # for email
import asyncio

cur_dir = os.getcwd()
log_dir = f"{cur_dir}/logs"
log_file = open(f"{log_dir}/down_server_logs.txt")
log_content = log_file.read()
down_server_list = json.loads(log_content)



# if list is empty
if str(down_server_list) == "[['']]": 
    sys.exit()


async def get_result():
    result = """Subject:Ansible_report\n\nThis is to notify you that the following servers are down:\n"""
    for server_group in down_server_list:
        for index, server in enumerate(server_group):
            server = server.split()
            result = result + f"Server #{index+1}: {server[0]} :  {server[1]}\n"
    return result

# result = get_result()

# print(result)

async def main():
    with open(f"{log_dir}/sent_down_server_logs.txt", "w") as file:
        file.write(log_content)

    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "ignacioaxelrom@gmail.com"
    receiver_email = "ignacioaxelrom@gmail.com"
    password = "oxxc xhra vniv srfu"
    message = await get_result()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

asyncio.run(main())
