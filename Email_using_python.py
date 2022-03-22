import smtplib

to_address = 'saivarmauddaraju333@gmail.com'
cc_list = ['umdvarma99@gmail.com']
bcc_list = ['arun.nadar@neosoftmail.com',
            "saivarma.uddaraju@yahoo.com",
            "ulpnagaraju@gmail.com"]
from_address = 'saivarmauddaraju@gmail.com'

message_subject = "Email assignment"
message_text = "This mail  is sent as a part of assignment"
message = "From: %s\r\n" % from_address \
          + "To: %s\r\n" % to_address \
          + "CC: %s\r\n" % ",".join(cc_list) \
          + "Bcc: %s\r\n" % ",".join(bcc_list) \
          + "Subject: %s\r\n" % message_subject \
          + "\r\n" + message_text

to_addresses_list = [to_address] + cc_list + bcc_list
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("saivarmauddaraju@gmail.com", "rugdjtcg")
server.set_debuglevel(1)
server.sendmail(from_address, to_addresses_list, message)
server.quit()
