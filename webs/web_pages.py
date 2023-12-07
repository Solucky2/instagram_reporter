class RegisterPageElements:
    """Elementy strony rejestracji"""

    email_input = '//*[@id="mount_0_0_nD"]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[4]/div/label/input'
    name_input = '//*[@id="mount_0_0_nD"]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[5]/div/label/input'
    username_input = '//*[@id="mount_0_0_nD"]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[6]/div/label/input'
    password_input = '//*[@id="mount_0_0_nD"]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[7]/div/label/input'


class LoginPageElements:
    """Elementy strony logowania"""

    email_input = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    password_input = '//*[@id="loginForm"]/div/div[2]/div/label/input'


class AccountPageElements:
    """Elementy strony użytkownia"""

    more_options_button = '//*[@id="mount_0_0_um"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div'
    report_button = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]'
    report_post = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]/div'
    report_account = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div'
    report_policy_wrong = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[3]/div'
    report_wrong_materials = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[1]/div'
    report_hate_speech = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[6]/div'
    send_report = '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/button'


class MainPageElements:
    """Elementy GUI głównego menu"""

    main_page_search = '//*[@id="mount_0_0_um"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div'
    main_page_search_input = '//*[@id="mount_0_0_um"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'


