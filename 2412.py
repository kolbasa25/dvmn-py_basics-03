import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("LOGIN")
token = os.getenv("TOKEN")

SENDER_EMAIL = "devmanorg@yandex.ru"
RECIPIENT_EMAIL = "utkinmihael@yandex.ru"

letter = """\
From: {sender}
To: {recipient}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.format(sender=SENDER_EMAIL, recipient=RECIPIENT_EMAIL)
letter = letter.replace("%website%", "https://dvmn.org/profession-ref-program/dezzzzlife/Z3cA4/")
letter = letter.replace("%friend_name%", "Вова")
letter = letter.replace("%my_name%", "Тимур")
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, token)
server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, letter)
server.quit()
