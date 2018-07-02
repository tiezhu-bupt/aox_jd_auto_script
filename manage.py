# -*- coding:utf-8 -*-
import requests
import logging
import click
from app.utils.base import Login
from app.utils.comment import ServerComment, ProductComment, AppendComment
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 禁用安全请求警告

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@click.group()
def cli():
    pass


@click.command()
def comment():
    login_result = Login().login()
    if login_result:
        logging.info('登录成功')

    # 服务评价
    ServerComment().start_comment()
    # 商品评价
    ProductComment().start_comment()
    # 追加评价
    AppendComment().start_comment()


cli.add_command(comment)

if __name__ == '__main__':
    cli()
