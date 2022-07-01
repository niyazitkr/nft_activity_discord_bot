from web3 import Web3
from web3.auto import w3
from web3.contract import ContractEvent
import time
import datetime
import os
import discord
from keep_alive import keep_alive
import requests
import json
import random
client = discord.Client()
from discord.ext import tasks
import asyncio
import urllib
import requests
from io import BytesIO
import io
previous_transaction = b'0'

#import niyaziasdasasda


avalanche_url = 'https://api.avax.network/ext/bc/C/rpc'
provider = Web3(Web3.HTTPProvider(avalanche_url))
print(provider.isConnected())
contract_address = '0x5378d068001D7E53D6c0a7ef539fbE213B5eB075'
abi = '[{"inputs":[{"internalType":"string","name":"nftName","type":"string"},{"internalType":"string","name":"nftSymbol","type":"string"},{"internalType":"string","name":"baseTokenURI","type":"string"},{"internalType":"address","name":"_royaltyRecipient","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_id","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"EARLY_NFT_PRICE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_MINTABLE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PER_CLAIM","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"NFT_PRICE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ROYALTY_VALUE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"canClaim","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"n","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"n","type":"uint256"}],"name":"earlyClaim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"earlyMint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"getAdmins","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_whitelistedAddress","type":"address"}],"name":"isEarlyMinter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"mainMintCountResult","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addressToWhitelist","type":"address"}],"name":"removeEarlyUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_addr","type":"address[]"}],"name":"setAdmins","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uri","type":"string"}],"name":"setBaseUri","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addresses","type":"address"},{"internalType":"uint256","name":"allowedToMint","type":"uint256"}],"name":"setEarlyMinters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_royaltyRecipient","type":"address"}],"name":"setRoyaltyAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"toggleClaimability","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"toggleEarlyMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

funnelheads = provider.eth.contract(contract_address, abi=abi)
print('Address:' + funnelheads.address)
print('Symbol:' + funnelheads.functions.symbol().call())
print('Name:' + funnelheads.functions.name().call())
print('Total Supply:' + str(funnelheads.functions.totalSupply().call()))

def get_activity_type(method_id):
  print(method_id)
  if method_id == '0x51ed8288':
    return "SOLD"
  elif method_id == '0xb88d4fde':
    return "LISTED"
  elif method_id == '0x40e58ee5':
    return "DELISTED"
  else:
    return "null"

def validate_event(amount,tr_from,tr_to):
  if((amount != 0) and (tr_to == str('0x11AC3118309A7215c6d87c7C396e2DF333Ae3A9C'))):
    return True
  else:
    return False


#event_filter = provider.eth.filter({"address": contract_address})

"""tx = provider.eth.get_transaction('0xde3b4d9a4cad6d30520cf876d46f7446808e94463ad913c5184e583f15a38fb7')
tx_value_wei = tx['value']
tx_value_eth = provider.fromWei(tx_value_wei, 'ether')
# Get address from and to
tx_from = tx['from']
tx_to = tx['to']
print (tx_value_eth, tx_from, tx_to)
validate_event(tx_value_eth, tx_from, tx_to)"""

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  asyncio.create_task(handle_events())
  #asyncio.create_task(handle_events_debug())

async def handle_events_debug():
  global sold_message
  global link_transaction_message
  global link_kalao_message
  global channel
  print("inside handle_event")
  task = asyncio.create_task(channel.send("Started searching NFT activities!"))
  await task
  token_id = 0
  tx = provider.eth.get_transaction('0x23bd79af8dad6ffb06797cd10389963dd4d431016952d81d73eef58e5024e27e')
  all_transactions = provider.eth.get_transaction_receipt('0x23bd79af8dad6ffb06797cd10389963dd4d431016952d81d73eef58e5024e27e')
  for index in range(len(all_transactions.logs)):
    if(len(all_transactions.logs[index].topics) == 4):
      token_id = int.from_bytes(all_transactions.logs[index].topics[3],byteorder='big')
      break
  tokenURI = funnelheads.functions.tokenURI(token_id).call()
  uri_json_link = "https://ipfs.io/ipfs/"+tokenURI.split("//")[1]
  with urllib.request.urlopen(uri_json_link) as url:
    data = json.loads(url.read().decode())
    print(data['name'])
    print(data['image'])
  token_name = data['name']
  tx_value_wei = tx['value']
  tx_value_eth = provider.fromWei(tx_value_wei, 'ether')
  token_rank = data['attributes'][0]['value']
  get_activity_type
  #if (True == validate_event (tx_value_eth, tx_from, tx_to)):
  sold_message = "SOLD-FH"+ str(token_name)+" -"+ str(tx_value_eth)+" Avax - Rank "+token_rank
  link_transaction_message = "https://snowtrace.io/tx/"'0x468c0db064bc6d01ca37978e75a81333b2340355a65a0cb8ee8c4342a56a073b'
  embed = discord.Embed(title=sold_message,url=link_transaction_message, color=discord.Color.blue())
  embed.set_author(name="Powered by Niyazi Toker", icon_url="https://ipfs.io/ipfs/QmUhaA6zHj8oEVydKqRtsa8SUvVWEaHTe6CNR5KraVcS8N")
  embed.add_field(name="Rank", value=data['attributes'][0]['value'], inline=True)
  embed.add_field(name="Rarity", value=data['attributes'][1]['value'], inline=True)
  embed.add_field(name="Backgrounds", value=data['attributes'][2]['value'], inline=True)
  embed.add_field(name="Funnels", value=data['attributes'][3]['value'], inline=True)
  embed.add_field(name="Body", value=data['attributes'][4]['value'], inline=True)
  embed.add_field(name="Eyes", value=data['attributes'][5]['value'], inline=True)
  embed.add_field(name="Faces", value=data['attributes'][6]['value'], inline=True)
  embed.add_field(name="Outfits", value=data['attributes'][7]['value'], inline=True)
  embed.set_image(url=data['image'])
  await channel.send(embed=embed)
  await asyncio.sleep(2)

async def retrieve_metadata(event,tx_value_eth,event_type):
  token_id = 0
  all_transactions = provider.eth.get_transaction_receipt(event['transactionHash'])
  for index in range(len(all_transactions.logs)):
    if(len(all_transactions.logs[index].topics) == 4):
      token_id = int.from_bytes(all_transactions.logs[index].topics[3],byteorder='big')
      break
  tokenURI = funnelheads.functions.tokenURI(token_id).call()
  uri_json_link = "https://ipfs.io/ipfs/"+tokenURI.split("//")[1]
  print(uri_json_link)
  with urllib.request.urlopen(uri_json_link) as url:
    data = json.loads(url.read().decode())
    print(data['name'])
    print(data['image'])
  token_name = data['name']
  sold_message = event_type +"-Funnelheads "+ str(token_name)+" - "+ str(tx_value_eth)+" Avax"
  #Discord message
  print(sold_message)
  embed = discord.Embed(title=sold_message,url = 'https://marketplace.kalao.io/collection/0x5378d068001d7e53d6c0a7ef539fbe213b5eb075', color=discord.Color.red())
  embed.set_author(name="Powered by Niyazi Toker", icon_url="https://ipfs.io/ipfs/QmUhaA6zHj8oEVydKqRtsa8SUvVWEaHTe6CNR5KraVcS8N")
  embed.add_field(name="Rank", value=data['attributes'][0]['value'], inline=True)
  embed.add_field(name="Rarity", value=data['attributes'][1]['value'], inline=True)
  embed.add_field(name="Backgrounds", value=data['attributes'][2]['value'], inline=True)
  embed.add_field(name="Funnels", value=data['attributes'][3]['value'], inline=True)
  embed.add_field(name="Body", value=data['attributes'][4]['value'], inline=True)
  embed.add_field(name="Eyes", value=data['attributes'][5]['value'], inline=True)
  embed.add_field(name="Faces", value=data['attributes'][6]['value'], inline=True)
  embed.add_field(name="Outfits", value=data['attributes'][7]['value'], inline=True)
  embed.set_image(url=data['image'])
  channel = client.get_channel(986291943929688129)
  await channel.send(embed=embed)


async def handle_events():
  global link_transaction_message
  print("inside handle_event")
  #task = asyncio.create_task(channel.send("Started searching NFT activities!"))
  #await task
  global previous_transaction
  block_filter = provider.eth.filter({'fromBlock':'latest', 'address':contract_address})
  while 1:
    for event in block_filter.get_new_entries():
      #asyncio.create_task( channel.send("New event!"))
      if(previous_transaction != event['transactionHash']):
        print("New event")
        previous_transaction = event['transactionHash']
        tx = provider.eth.get_transaction(event['transactionHash'])
        tx_from = tx['from']
        tx_to = tx['to']
        tx_value_wei = tx['value']
        tx_value_eth = provider.fromWei(tx_value_wei, 'ether')
        print(tx_from,tx_to,tx_value_eth)
        #if (True == validate_event (tx_value_eth, tx_from, tx_to)):
        event_type = get_activity_type(tx['input'][0:10])
        if ('null' != event_type):
          print("Valid event")
          asyncio.create_task(retrieve_metadata(event,tx_value_eth,event_type))
          await asyncio.sleep(2)

    
priv_token = os.environ['BOT_TOKEN']
keep_alive()
client.run(priv_token)
print("AFTER CLINTR")


