from datetime import datetime
from playwright.sync_api import sync_playwright

from present_controll.resource_connection import ResourseConnection


class PlayWrightConnection(ResourseConnection):
    def __enter__(self):
        # Запуск без контекстного менеджера с ручным .stop()
        p = sync_playwright().start()
        self.browser = p.firefox.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.set_default_timeout(20_000)
        self.page.goto(self.path)
        return self

    def get_content(self, it):
        replace_dot_date = f"{it}".replace('.', ' ')

        a = datetime.strptime(replace_dot_date, "%d %m %Y")
        now_date = datetime.now()

        for _ in range((now_date - a).days // 10):
            try:
                self.page.get_by_text('Показать больше матчей').click()
            except Exception:
                break
        return self.page.content()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()


if __name__ == '__main__':
    with PlayWrightConnection('https://www.livesport.com/ru/basketball/usa/nba/results/') as c:
        with open('test.html', 'w', encoding='UTF-8') as f:
            f.write(c.get_content('14.12.2023'))
    print('Готово!')
