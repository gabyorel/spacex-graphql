import enum

from aiohttp import BasicAuth
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from grphql.query import (
    GET_COMPANY_INFO
)

class AuthType(enum.Enum):
    NONE = 0
    BASIC = 1
    APIKEY = 2

auth_methods = {
    AuthType.NONE: 'none',
    AuthType.BASIC: 'basic',
    AuthType.APIKEY: 'apikey'
}


class GraphQLClient:
    def __init__(
        self,
        url,
        username = None,
        password = None,
        auth_type = 'none',
        api_key = None,
        headers = {}
    ) -> None:

        self.url = url
        self.headers = headers

        if url is None:
            raise ValueError('URL must be provided')

        if auth_type not in auth_methods.values():
            raise ValueError(
                'Auth type must be one of ' + ', '.join(auth_methods.values())
            )

        if (username is None or password is None) and auth_type == auth_methods[AuthType.BASIC]:
            raise ValueError(
                'Username and password must be provided for basic auth'
            )

        if auth_type == auth_methods[AuthType.APIKEY]:
            if api_key is None:
                raise ValueError(
                    'API key must be provided for api based auth'
                )

            self.headers.update({
                'Authorization': 'ApiKey ' + api_key
            })

        self._transport = AIOHTTPTransport(
            url = self.url,
            auth = BasicAuth(username, password) \
              if auth_type == auth_methods[AuthType.BASIC] else None,
            headers = self.headers
        )
        self._client = Client(
            transport = self._transport,
            fetch_schema_from_transport = True
        )

    async def get_company_info(self):
        query = gql(GET_COMPANY_INFO)

        async with self._client as session:
            result = await session.execute(query)
            return result
