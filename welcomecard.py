import discord
from discord.ext import commands
import os
import easy_pil
import random

class WelcomeCard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("WelcomeCard Cog Loaded")
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
         
         welcome_channel = member.guild.system_channel
         images = [image for image in os.listdir("./Cogs/Images")]
         randomized_image = random.choice(images)

         bg = easy_pil.Editor(f"./Cogs/Images/{randomized_image}").resize(1920, 1080)
         avatar_image = await easy_pil.load_image_async(str(member.avatar.url))
         avatar = easy_pil.Editor(avatar_image).resize((250, 250)).circle_image()

         font_big = easy_pil.Font.poppins(size=90, variant="bold")
         font_small = easy_pil.Font.poppins(size=60, variant="bold")

         bg.paste(avatar, (835, 340))
         bg.ellipse((835, 340), 250, 250, outline="white", stroke_width=5)

         bg.text((960, 620), f"Welcome to {member.guild.name}!", color="white", font=font_big, align="center")
         bg.text((960, 740), f"{member.name} is member #{member.guild.member_count}!", color="white", font=font_small, align="center")

         img_file = discord.File(fp=bg.image_bytes, filename=randomized_image)

         await welcome_channel.send(f"Ni Hao {member.name}! Welcome to {member.guild.name}!")
         await welcome_channel.send(file=img_file)

async def setup(bot):
        await  bot.add_cog(WelcomeCard(bot))