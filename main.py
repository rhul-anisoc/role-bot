import discord
import dotenv
import os


class OscarClient(discord.Client):

    async def on_ready(self):
        self.role_id = os.environ["ROLE_ID"]

        print(f"Connected as {self.user}")
        print(f"ROLE_ID = {self.role_id}")

    async def on_presence_update(self, before: discord.Member, after: discord.Member):
        try:
            role = discord.utils.get(before.guild.roles, id=self.role_id)
            member = self.get_guild(before.guild.id).get_member(before.id)

            print(
                f"{member.name} - Pending: (Before: {before.pending}) (After: {after.pending})")

            if (before.bot) or (after.bot):
                return

            if before.pending and not after.pending:
                print(f"Gave role to {member.name}")
                await member.add_roles(role, atomic=True)

        except Exception as e:
            print("things are not good", e)


if __name__ == "__main__":
    dotenv.load_dotenv()

    inte = discord.Intents.default()
    inte.presences = True
    inte.members = True
    client = OscarClient(intents=inte)
    client.run(os.environ['TOKEN'])
