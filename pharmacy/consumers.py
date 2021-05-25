import asyncio
from channels.generic.websocket import AsyncConsumer
from .models import Item, CheckedItem, Check
from channels.db import database_sync_to_async
from channels.db import SyncToAsync
from random import randint
import json
from datetime import datetime,date

class WSconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connect', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('receive', event)
        textdata = json.loads(event.get('text', None))
        print(textdata)
        codetext = textdata['code']
        checkidtext = textdata['checkid']
        if codetext is not None:
            print(codetext)
            await self.get_items_andedit(codetext, checkidtext)
            itemdata = await self.get_checked_item(codetext)
            iteminfo = {
                'name': itemdata.name,
                'price': itemdata.price
            }
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps(iteminfo)
            })


    async def websocket_disconnect(Self,event):
        print('disconnected', event)

    @database_sync_to_async
    def get_items_andedit(self,c,id):
        product = Item.objects.get(code=c)
        product.amount -= 1 
        checkproduct = CheckedItem(name=product.name,price=product.price,code=product.code,pub_date=datetime.now(),amount=1)
        product.save()
        checkproduct.save()
        check = Check.objects.get(id=id)
        checkproduct.check_set.add(check)


    @database_sync_to_async
    def get_checked_item(self,c):
        return CheckedItem.objects.get(code=c)



    

        



