from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from PilLite import Image


def text_from_img():
    img = Image.open('travinka-bozhi-korovki.jpg')
    print(img.size)
    img.thumbnail((200, 200))
    img.save('size.jpg')


if __name__ == '__main__':
    print(date.today())
    calculate_salary()
    get_employees()
    text_from_img()
