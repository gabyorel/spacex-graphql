import os
import json
import asyncio

from grphql.client import GraphQLClient

async def main():

    url = os.getenv("GRAPHQL_URL")
    key = os.getenv("GRAPHQL_API_KEY")

    client = GraphQLClient(
        url = url,
        auth_type = 'basic',
        username = 'ApiKey',
        password = key,
        headers = {
            "x-cache-control": "no-cache"
        }
    )

    result = await client.get_company_info()

    print(
        json.dumps(
            result,
            indent=2
        )
    )

asyncio.run(main())