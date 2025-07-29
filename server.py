import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/zappos1'

mcp = FastMCP('zappos1')

@mcp.tool()
def brands_list() -> dict: 
    '''List all brands from Zappos'''
    url = 'https://zappos1.p.rapidapi.com/brands/list'
    headers = {'x-rapidapi-host': 'zappos1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List products, search products with options and filters'''
    url = 'https://zappos1.p.rapidapi.com/products/list'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'zappos1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def products_detail(productId: Annotated[str, Field(description='Get id value from products/list API')]) -> dict: 
    '''Get detail information of product by productId'''
    url = 'https://zappos1.p.rapidapi.com/products/detail'
    headers = {'x-rapidapi-host': 'zappos1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'productId': productId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def categories_list() -> dict: 
    '''List all categories from Zappos'''
    url = 'https://zappos1.p.rapidapi.com/categories/list'
    headers = {'x-rapidapi-host': 'zappos1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
