from telethon import TelegramClient
from dotenv import load_dotenv
import argparse
import os


def building_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-c", "--chat",
        type=str,
        required=True,
        help="target chat for export"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="export output file"
    )
    return parser.parse_args()


async def main(target_chat:str,output_file: str):
    target_chat = int(target_chat)
    with open(output_file, "a", encoding="utf-8") as f:
        async for message in client.iter_messages(target_chat, reverse=True):
            if message.text:
                f.write(message.text + "\n")


if __name__ == "__main__":
    load_dotenv()

    args = building_args()

    telegram_api_id = int(os.getenv("TELEGRAM_API_ID"))
    telegram_api_hash = os.getenv("TELEGRAM_API_HASH")

    client = TelegramClient(
        "session",
        telegram_api_id,
        telegram_api_hash
    )

    with client:
        client.loop.run_until_complete(
            main(args.chat, args.output)
        )
