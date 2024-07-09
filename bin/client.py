from discogs_client import Client

class DiscogClient:

    def __init__(self, user_agent : str, user_token : str) -> None:
        try:
            self._instance = Client(user_agent=user_agent, user_token=user_token)
            self._instance.set_timeout(
                connect =  30,
                read =  30,
            )
        except:
            print('[lib / discogs_client] Failed to initialize Discogs Client.')

    def instance(self):
        return self._instance