# importing libraries
import smtplib
from configparser import ConfigParser


def main():
    file = "config.ini"
    config = ConfigParser()
    config.read(file)

    def email_smtp():

        message = "From: %s\r\n" % from_address \
                  + "To: %s\r\n" % to_address \
                  + "CC: %s\r\n" % ",".join(cc_list) \
                  + "Bcc: %s\r\n" % ",".join(bcc_list) \
                  + "Subject: %s\r\n" % message_subject \
                  + "\r\n" + message_text

        to_addresses_list = [to_address] + cc_list + bcc_list
        server = smtplib.SMTP('smtp.gmail.com')  # simple mail transfer protocol
        server.starttls()  # for making secure connection
        server.login(config["login"]["user_name"], config["login"]["password"])
        server.set_debuglevel(1)
        server.sendmail(from_address, to_addresses_list, message)
        server.quit()

    to_address = config["email"]["to"]
    cc_list = [config["email"]["cc"]]
    bcc_list = [config["email"]["bcc"]]
    from_address = config["email"]["from"]

    message_subject = config["email"]["subject"]
    message_text = config["email"]["text"]
    email_smtp()

if __name__ == '__main__':
    main()
