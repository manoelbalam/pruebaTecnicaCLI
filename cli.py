#!/usr/bin/python3

import click, requests

@click.command()
@click.option('-b','--backend', prompt=True, required=True, help='Backend address ex. localhost:8000')
@click.option('-e','--endpoint', prompt=True, required=True, type=click.Choice(['signup', 'login'], case_sensitive=False))
@click.option('-u','--useraccess', prompt=False, help='UserAccess')
@click.option('-p','--passaccess', prompt=False, hide_input=True,confirmation_prompt=True, help='PassAccess')
@click.option('-d','--date', prompt=False, type=str,help='date format YYYY-MM-DD [optional]')

def ptCLI(backend,endpoint,useraccess,passaccess,date):

    if endpoint == 'signup':
        url = 'http://' + backend + '/api/Seguridad/' + endpoint + '/'
        if not useraccess or not passaccess:
            res = requests.get(url = url)
            click.echo(f'{res.json()}')
        else:
            res = requests.post(url = url, json = {'UserAccess':useraccess,'PassAccess':passaccess, 'ExpirationAccess':date})
            click.echo(f'{res.json()}')

    if endpoint == 'login':
        url = 'http://' + backend + '/api/Seguridad/' + endpoint + '/'
        res = requests.post(url = url, json = {'UserAccess':useraccess,'PassAccess':passaccess})
        click.echo(f'{res.json()}')

if __name__ == '__main__':
    ptCLI()