from printer import TruthTable,KMap
from graycode import *
import click
# global equation
# equation = None

@click.group()
def cli():
      pass


@cli.command()
@click.argument('eqn',type=str)
@click.option('--kmap',is_flag=True)
@click.option('--table',is_flag=True)
def equation(eqn,kmap,table):
      
      if kmap:
            myfunc = KMap(eqn)
            click.echo(myfunc.printKMap())
      
      if table:
            myfunc = TruthTable(eqn)
            click.echo(myfunc.printTable())

@cli.command()
@click.option('-bd','--bindec',type=str)
@click.option('-db','--decbin',type=int)
@click.option('-bg','--bingray',type=str)
def conv(bindec,decbin,bingray):
      
      if bindec:
            click.echo("Binary to decimal of {} : ".format(bindec) + str(binTodec(bindec)))
      
      if decbin:
            click.echo("Decimal to binary of {} : ".format(bindec) + str(decTobin(decbin)))

      if bingray:
            click.echo("Binary to graycode of {} : ".format(bingray) + str(conv_grayCode(bingray)))

      

if __name__ == "__main__":
    cli()






