import sys
from .uploader import upload_image
from .url_converter import url2imgurl, url2tag
import click


@click.group()
def main():
    pass


@click.command()
@click.argument('file_path')
def url(file_path):
    file_id = upload_image(file_path)
    click.echo(url2imgurl(file_id))


@click.command()
@click.argument('file_path')
def tag(file_path):
    file_id = upload_image(file_path)
    click.echo(url2tag(file_id))


main.add_command(url)
main.add_command(tag)

if __name__ == '__main__':
    main()
