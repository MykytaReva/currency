from faker import Faker
fake = Faker()


def mail_name():
    nm = fake.first_name()
    email = fake.email()
    result = f'{nm} {email}<br/>'
    return result


def generate():
    lis = []
    for _ in range(10):
        lis.append(mail_name())
    x = ''.join(map(str, lis))
    return x
