from pizza import *
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f'Готовим Вашу пиццу {pizza} за 20 минут')
    if delivery:
        print('Доставим Вашу пиццу за 50 минут')


@cli.command()
def menu():
    """Выводит меню"""
    print(f' - 🧀 The most cheesy Margherita in your life: {Margherita().dict()}')
    print(f' - 🌶 The most piquant Pepperoni in the world: {Pepperoni().dict()}')
    print(f' - 🍍 The sweetest Hawaiian in the galaxy: {Hawaiian().dict()}')
    print(f' - 🥕 Baby carrots for your little companions: {BabyCarrot().dict()}')


if __name__ == '__main__':
    cli()
