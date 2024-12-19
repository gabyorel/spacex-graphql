import os
import asyncio

from aiohttp import BasicAuth
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

async def main():

    url = os.getenv("GRAPHQL_URL")
    key = os.getenv("GRAPHQL_API_KEY")

    transport = AIOHTTPTransport(
        url = url,
        auth = BasicAuth("ApiKey", key)
    )

    async with Client(
        transport = transport,
        fetch_schema_from_transport = True
    ) as session:
        
        query = gql(
            """
            query GetCompanyInfo {
              company {
                founder
                founded
                launch_sites
                headquarters {
                  address
                  city
                  state
                }
                name
                valuation
                vehicles
              }
            }
        """
        )

        result = await session.execute(query)
        print(result)

asyncio.run(main())