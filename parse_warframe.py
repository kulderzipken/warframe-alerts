from bs4 import BeautifulSoup
from url_request import simple_get
from send_emails import send_mail
from send_sms import send_text
import time

#pc : https://deathsnacks.com/wf/
#ps : https://deathsnacks.com/wfps4/


def check_alerts(item):
    raw_html = simple_get('https://deathsnacks.com/wfxb1/')
    while True:
        html = BeautifulSoup(raw_html, 'html.parser')
        for li in html.select('li'):
            try:
                if li['class'] == ['list-group-item']:
                    for span in li.select('span'):
                        try:
                            if span['class'] == ['badge']:
                                if span.text == item:
                                    print("Item in Alert now!")
                                    send_mail(item)
                                    send_text(item)
                                    print("mesages sent! waiting half an hour")
                                    time.sleep(1800)
                                    print("30 min wait is over!")
                                    continue
                        except KeyError:
                            pass
            except KeyError:
                pass
        print ("waiting 60 seconds")
        time.sleep(60)
        print ("wait is over")
        continue

if __name__ == '__main__':
    check_alerts('Nitain Extract')


   

