from printer import TruthTable,KMap,Minterms
from graycode import *
import click
# global equation
# equation = None

@click.group()
def cli():
      pass


@cli.command(help="<Equation in terms of Literals> [--kmap] [--table]")
@click.argument('eqn',type=str)
@click.option('--kmap',is_flag=True,help="For showing kmap")
@click.option('--table',is_flag=True,help="For showing table")
def equation(eqn,kmap,table):
      
      if kmap:
            myfunc = KMap(eqn)
            click.echo(myfunc.printKMap())
      
      if table:
            myfunc = TruthTable(eqn)
            click.echo(myfunc.printTable())

@cli.command(help="[OPTION for convertion] <number>")
@click.option('-bd','--bindec',type=str,help="Converting binary number to decimal")
@click.option('-db','--decbin',type=int,help="Converting decimal number to binary")
@click.option('-bg','--bingray',type=str,help="Converting binary number to Graycode")
def conv(bindec,decbin,bingray):
      
      if bindec:
            click.echo("Binary to decimal of {} : ".format(bindec) + str(binTodec(bindec)))
      
      if decbin:
            click.echo("Decimal to binary of {} : ".format(bindec) + str(decTobin(decbin)))

      if bingray:
            click.echo("Binary to graycode of {} : ".format(bingray) + str(conv_grayCode(bingray)))

@cli.command(help="<Number of Literals> <Minterms seperated by ','> [--kmap] [--table]")
@click.argument('number',type=int)
@click.argument('minTerms',type=str)
@click.option('--kmap',is_flag=True,help="For showing KMap")
@click.option('--table',is_flag=True,help="For showing Table")
def minterms(number,minTerms,kmap,table):
      s = minTerms
      s = s.split(',')
      s = [int(j) for j in s]
      t1 = Minterms(number,s)

      if kmap:
            click.echo(t1.generateTable())

      if table:
            click.echo(t1.printKMap())


if __name__ == "__main__":
    cli()






