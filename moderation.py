import discord
from discord.ext import commands
from discord import app_commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod Cog Loaded")

    @app_commands.command(name="clear", description="Clears a specified amount of messages in a channel.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def delete_messages(self, interaction: discord.Interaction, amount: int):
        if amount < 1:
            await interaction.response.send_message("You must delete at least one message.")
            return
        await interaction.response.send_message(f"{interaction.user.mention} has cleared {amount} messages.", ephemeral=False)

    @app_commands.command(name="kick", description="Kicks a member from the server.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.kick(member)
        await interaction.response.send_message(f"{interaction.user.mention} has kicked {member.mention} from the server.", ephemeral=False)

    @app_commands.command(name="ban", description="Bans a member from the server.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.ban(member)
        await interaction.response.send_message(f"{interaction.user.mention} has banned {member.mention} from the server.", ephemeral=False)

    @app_commands.command(name="unban", description="Unbans a member from the server by their User ID.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user_id: str):
        user = await self.bot.fetch_user(user_id)
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"{interaction.user.mention} has banned {user.name} from the server.", ephemeral=False)

    @app_commands.command(name="mute", description="Mutes a user.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member):
        muted_role = interaction.guild.get_role(1395769862357258392)
        await member.add_roles(muted_role)
        await interaction.response.send_message(f"{member.mention} has been muted.", ephemeral=False)

    @app_commands.command(name="unmute", description="Unmutes a user.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def unmute(self, interaction: discord.Interaction, member: discord.Member):
        muted_role = interaction.guild.get_role(1395769862357258392)
        await member.remove_roles(muted_role)
        await interaction.response.send_message(f"{member.mention} has been unmuted.", ephemeral=False)


async def setup(bot):
    await bot.add_cog(Mod(bot))