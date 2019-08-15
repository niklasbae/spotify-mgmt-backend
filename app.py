from flask import Flask, redirect, request
from flask_restplus import Api, Resource, fields
import requests
import json
import urllib.parse


app = Flask(__name__)
api = Api(app)

clientId = "ef88e63c8bd44b0d9a49168864c6b298"
clientSecret = "56e3cb3c64e14edb98d3d2ce1b7772e4"
redirectUrlDev = "http://localhost:5000/callback"
redirectUrl = "https://spotify-mgmt-backend.herokuapp.com/callback"



a_language = api.model('language', {'language' : fields.String('The language.')})


languages = []
python = {'language' : 'Python'}
languages.append(python)

@api.route('/language')
class Language(Resource):
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201


@api.route('/login')
class Login(Resource):
    def get(self):

        return redirect("https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fclient_id%3D" + clientId + "%26response_type%3Dcode%26redirect_uri%3D" + urllib.parse.quote(redirectUrl) + "%26scope%3Dplaylist-read-private")

@api.route('/callback')
class Callback(Resource):
    def get(self):

        code = request.args.get('code')

        url = "https://accounts.spotify.com/api/token"

        payload = "grant_type=authorization_code&code=" + code + "&redirect_uri=" + urllib.parse.quote(redirectUrl) + "&client_id=" + clientId + "&client_secret=" + clientSecret
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)


        return response.json()


if __name__ == '__main__':
    app.run(debug=True)