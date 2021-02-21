"""
Defines external http requests over the web.
"""
# import json
import requests


class GraphQLQuery:
    """
    Defines methods for reading data from GraphQL based enpoints.
    """

    @staticmethod
    def get_top_10():
        url = 'https://flagship-api.herokuapp.com/graphql/'
        payload = '''
        query{
            maradonaScores {
                playerName
                steps
                gameDatetime
            }
        }
        '''
        response = requests.post(url, json={'query': payload})

        return response.json()


class GraphQLMutation():

    @staticmethod
    def register_score(username, steps):
        url = 'https://flagship-api.herokuapp.com/graphql/'
        payload = f'''
        mutation {{
            createMaradonaScore( input: {{
                playerName: "{username}"
                steps: {steps}
            }}) {{
                score {{
                    playerName
                    steps
                    gameDatetime
                }}
            }}
        }}
        '''
        response = requests.post(url, json={'query': payload})

        return response.json()
