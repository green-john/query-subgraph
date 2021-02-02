import requests
import pprint

import sys

from datetime import datetime

def print_one_swap(swap):
    unidex_in = float(swap['amount0In'])
    unidex_out = float(swap['amount0Out'])

    weth_in = float(swap['amount1In'])
    weth_out = float(swap['amount1Out'])

    ts = datetime.fromtimestamp(int(swap['timestamp']))

    print(ts.strftime("%Y-%m-%d:%H:%M:%S"), "", end="")

    if unidex_in == 0:
        xchange_rate = weth_in / unidex_out
        print(f"{weth_in} WETH -> {unidex_out} UNIDX ({xchange_rate})")
    else:
        xchange_rate = weth_out / unidex_in
        print(f"{unidex_in} UNIDX -> {weth_out} WETH ({xchange_rate})")

def main():
    params = {
        # "refToken": "0x111111111117dc0aa78b770fa6a738034120c302" # 1INCH
        "refToken": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", #WETH
        "targetToken": "0x95b3497bbcccc46a8f45f5cf54b0878b39f8d96c", #UNIDX
        # "pairId": "0x26aad2da94c59524ac0d93f6d6cbf9071d7086f2", #WETH-1INCH
        "pairId": "0xe236416af855196acb1cd16712a2311ccc9c950d" #WETH-UNIDX
    }

    query = ""
    with open(sys.argv[1], "r") as f:
        query = f.read()

    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    response = requests.post(url, json={
        "query": query,
        "variables": params
    })

    print(response.status_code)
    swaps = response.json()['data']['swaps']
    list(map(print_one_swap, swaps))

if __name__ == '__main__':
    main()
