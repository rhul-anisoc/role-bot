import discord
import dotenv
import os


class OscarClient(discord.Client):

    def __init__(self):
        self.role_id = os.environ["ROLE_ID"]

    async def on_ready(self):
        print(f"Connected as {self.user}")
        print(f"ROLE_ID = {self.role_id}")

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        try:
            role = discord.utils.get(before.guild.roles, id=self.role_id)
            member = self.get_guild(before.guild.id).get_member(before.id)

            if (before.bot) or (after.bot):
                return

            if before.pending and not after.pending:
                await member.add_roles(role, atomic=True)

        except Exception as e:
            print("things are not good", e)


if __name__ == "__main__":
    dotenv.load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True
    client = OscarClient(intents=intents)
    client.run(os.environ['TOKEN'])
