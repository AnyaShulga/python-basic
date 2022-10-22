"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', endpoint="index_page")
def get_homepage():
    title="Index"
    return render_template("base.html", title=title)


@app.route('/about/', endpoint="about")
def get_about():
    title="Lorem Ipsum"
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
           "Donec pretium tincidunt tempor. Mauris sed molestie urna. " \
           "Nam nec mattis tellus. Etiam euismod purus id bibendum efficitur. " \
           "Vivamus eu est ipsum. Morbi ultrices eu ligula sit amet sagittis. " \
           "Suspendisse potenti. Suspendisse ut mi hendrerit, pellentesque sem a, iaculis leo. " \
           "Donec efficitur dolor sit amet erat tempor maximus. " \
           "Ut metus eros, ullamcorper vel ultricies ut, vulputate convallis risus."
    return render_template("base.html", title=title, text=text)


if __name__ == '__main__':
    app.run(debug=True)