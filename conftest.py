import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# добавляем обработчики для передачи инфо через командную строку в функции pytest_addoption
def pytest_addoption(parser):
    # выбор браузера для запуска тестов
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # выбор языка для браузера
    parser.addoption('--language', action='store', default='en',
                     help='Choose the language: ru, en ... or etc.',)

# фикстура вызывается в тестах, где передан параметр browser
@pytest.fixture(scope="function")
def browser(request):
    # задаем в переменную запрос, ожидающий параметр браузера
    browser_name = request.config.getoption("browser_name")
    browser = None
    # задаем в переменную запрос, ожидающий параметр языка
    user_language = request.config.getoption("language")
    if browser_name == 'chrome':
        print("\nstart Chrome browser for test")
        # для указания языка браузера используем класс Options и метод add_experimental_option
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\nstart Firefox browser for test")
        # для указания языка браузера используем методы FirefoxProfile и set_preference
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser")
    browser.quit()

# Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser.
# Фикстура передается в тестовый метод в качестве аргумента.
# Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.