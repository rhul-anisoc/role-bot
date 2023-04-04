import discord
import dotenv
import os


class OscarClient(discord.Client):
    async def on_ready(self):
        print(f"Connected as {self.user}")

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        try:
            role_id = os.environ["RoleID"]
            role = discord.utils.get(before.guild.roles, id=role_id)
            member = self.get_guild(before.guild.id).get_member(before.id)

            if (before.bot) or (after.bot):
                return

            if before.pending:
                if not after.pending:
                    await member.add_roles(role, atomic=True)

        except Exception as e:
            print("things are not good", e)


if __name__ == "__main__":
    dotenv.load_dotenv()
