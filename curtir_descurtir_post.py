from login import *







def like_unlike_user_post():

    url = input('Insira o URL da conta do Instagram: ')
    action = ''
    while action not in {'curtir', 'descurtir'}:
        action = input('Digite a ação (curtir/descurtir): ').lower()

    login()

    driver.get(url)

    sleep(3)







if __name__ == "__main__":
    like_unlike_user_post()