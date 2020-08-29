from printer import TruthTable,KMap

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
def result(eqn,kmap,table):
      
      if kmap:
            myfunc = KMap(eqn)
            click.echo(myfunc.printKMap())
      
      if table:
            myfunc = TruthTable(eqn)
            click.echo(myfunc.printTable())

if __name__ == "__main__":
    cli()






