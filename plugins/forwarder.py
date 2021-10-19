# HuzunluArtemis

from pyrogram import Client, filters
from HelperFunc.authUserCheck import AuthUserCheck
from HelperFunc.forceSubscribe import ForceSub
from HelperFunc.messageFunc import copyMessage
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.all)
async def forward(client, message):
	if not await AuthUserCheck(message.chat.id, message.from_user.id): return
	if await ForceSub(client, message) == 400: return
	await copyMessage(message)
	